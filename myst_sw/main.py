##
# myst_main.py -- Where it all begins...
#
# On a less glamorous note, this file was renaimed main.py on December 2019 for
# compatibility with micropython. Will revisit this once we scale up.
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

import network
from time import sleep

from initialize import *
from pump import *

networkSSID = 'iRobot-Guest'
networkPsswd = ''

networkConTimeout = 10
networkTmrInc = 0.1

squirtDuration = 5 # How long should the pump squirt for

class NetworkError(BaseException):
    pass

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
        squirt(squirtDuration)

if __name__ == "__main__":

    main()





