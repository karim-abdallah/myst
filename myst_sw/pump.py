##
# pump.py -- *insert short description* 
#
# Written by Karim Abdallah on Wednesday, 11 December 2019.
##

from time import sleep
from hal import *

def squirt(duration):

    print("Squirt Squirt")
    pump_on()
    sleep(duration)
    pump_off()

    return True
