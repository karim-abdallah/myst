##
# myst_main.py -- Where it all begins...
#
# On a less glamorous note, this file was renaimed main.py on December 2019 for
# compatibility with micropython. Will revisit this once we scale up.
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

from machine import Pin
from time import sleep
import network

networkSSID = 'iRobot-Guest'
networkPsswd = ''

pump = Pin(5, Pin.OUT)

networkConTimeout = 10
networkTmrInc = 0.1

squirtDuration = 5 # How long should the pump squirt for

class NetworkError(BaseException):
    pass

def initializePump ():
    print("Pump Succesfully Initialized")

def initializeChirp ():
    print("Chirp Successfully Initialized")

def configureNetwork ():
    
    wlan = network.WLAN(network.STA_IF)
    networkTimer = 0;
    
    wlan.active(True)
    
    if not wlan.isconnected():
        print("connecting to network", networkSSID, networkPsswd)
        wlan.connect(networkSSID, networkPsswd)

    while (not wlan.isconnected() and networkTimer < networkConTimeout):
        sleep(networkTmrInc)
        networkTimer += networkTmrInc
        
    if not wlan.isconnected():
        print("Couldn't connect to the network")
    else:
        print("Network Succesfully Configured.")
        print("network config:", wlan.ifconfig())
  
def pump_on():
    pump.on()

def pump_off():
    pump.off()

def squirt(duration):

    print("Squirt Squirt")
    pump_on()
    sleep(duration)
    pump_off()

    return True

def main():

    configureNetwork()
    initializePump()
    initializeChirp()

    while True:
        squirt(squirtDuration)

if __name__ == "__main__":

    main()





