##
# connectivity.py -- This file contains all network and connectivity related functions and modules.
#
# Written by Karim Abdallah on Wednesday, 11 December 2019.
##


import network
from time import sleep

networkSSID = 'iRobot-Guest'
networkPsswd = ''

networkConTimeout = 10
networkTmrInc = 0.1

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


