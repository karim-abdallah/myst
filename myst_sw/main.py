##
# myst_main.py -- *insert short description* 
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

from machine import Pin
from time import sleep
import network

networkSSID = 'iRobot-Guest'
networkPsswd = ''

motor = Pin(5, Pin.OUT)

networkConTimeout = 10
networkTmrInc = 0.1

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
  


def main():

    configureNetwork()
    initializePump()
    initializeChirp()

    while True:
        print("motor switch")
        motor.value(not motor.value())
        sleep(5)

if __name__ == "__main__":

    main()





