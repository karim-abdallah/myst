##
# myst_main.py -- Where it all begins...
#
# On a less glamorous note, this file was renaimed main.py on December 2019 for
# compatibility with micropython. Will revisit this once we scale up.
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

import machine
import ntptime

from time import sleep

from initialize import *
from pump import *
from connectivity import *

squirtDuration_sec = 2*60 # How long the pump should squirt for

rtc = machine.RTC()

# TODO: figure out what happened at index number 3... seems to follow date but otherwise a bit weird...

yearIndex = 0
monthIndex = 1
dayIndex = 2
hourIndex = 4
minIndex = 5
secIndex = 6


# TODO: make this list user-appendable. This should be a feature in the future (scheduling)
# Potentially also expand it to which day of the week (might be tricky but worth the try)

hourSchedule = [13, 15, 20] # in UTC time (for NY time, substract 6 hours]
daySchedule = 4 # for now, fixed interval for squirting.
hourMaximum = 23 # designates when we've reached the end of a watering period

# TODO: create wrappers around rtc.datetime()[hour... to ease of writing

def rtcHour():
    return rtc.datetime()[hourIndex]

def rtcMin():
    return rtc.datetime()[minIndex]

def rtcSec():
    return rtc.datetime()[secIndex]

def printTime():
    print("the time right now is: ", rtc.datetime()[hourIndex], "h ", rtc.datetime()[minIndex], "min and ", rtc.datetime()[secIndex], "seconds")

    
def main():

    configureNetwork()
    initializePump()
    initializeChirp()

    # TODO: create two seperate "modes" for whether scheduling is active or not, based on connectivity.
    # Scheduling shouldn't be available if there is no connectivity.

    if not isConnected():
        rtc.datetime((2015, 1, 1, 3, 0, 0, 0, 0)) # Set time as Jan 1st 2015. Scheduling features inactive.

    else:
        ntptime.settime()
        
    # print(rtc.datetime())

    dayNow = rtc.datetime()[dayIndex]
    hourNow = rtc.datetime()[hourIndex]
    minNow = rtc.datetime()[minIndex]
    secNow = rtc.datetime()[secIndex]

    waterToday_b = False

    dayCounter = 0
    hourCounter = 0

    printTime()

    print ("Starting Main application. It's Moist.")

    while True:

        # Begin to countdown the time. Keep track of every day change and increment the relevant counter.
        # When we've reached our scheduled day, flag and count the hours.
        # When we've reached our scheduled our, squirt. Keep doing so until the full 24 hour period has
        # elapsed, after which reset the our counter and return to keeping track of the days elapsed.
        if ((rtc.datetime()[dayIndex] - dayNow) is not 0):
            print ("One more day passed")
            dayCounter += 1
            print("Day counter = ", dayCounter)
            dayNow = rtc.datetime()[dayIndex]
            printTime()

        # TODO: try implementing logic that allows for scheduling by day of the week. With a list for example.
        # The only thing to figure out is how to reset the day counter once we reach the end of the week
        # Harder to do than hours because we have to make sure we're still watering. Maybe reset the day
        # counter at the end of the 23 hour period.
        
        if (dayCounter >= daySchedule):
            print ("Today, we water!")
            waterToday_b = True
            dayCounter = 0
            hourNow = rtc.datetime()[hourIndex]
            printTime()

        if (waterToday_b and ((rtc.datetime()[hourIndex] - hourNow) is not 0)): 
            print ("One more hour passed")
            hourCounter += 1
            hourNow = rtc.datetime()[hourIndex]
            printTime()

        if (waterToday_b and (hourCounter in hourSchedule)):
            squirt(squirtDuration_sec)
            printTime()

        if (hourCounter >= hourMaximum):
            print ("What a wonderful day of gardening it was! See you next time!")
            hourCounter = 0
            waterToday_b = False
            printTime()
            
            

# Note: The following is commented out code for prototyping. This works and squirts every minute.       

#       if ((rtc.datetime()[minIndex] - minNow) >= 1):
#           print("we are at ", minNow, " minutes")
#           squirt(squirtDuration_sec)
#           minNow = rtc.datetime()[minIndex]
#           print("the new minute variable is: ", minNow)
#           print("Done squirting.")
#           printTime()

#        if (interval >= 1):
#            squirt(squirtDuration_sec)
#            interval = 0

        

if __name__ == "__main__":

    main()





