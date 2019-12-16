##
# connectivity.py -- This file contains all network and connectivity related functions and modules.
#
# Written by Karim Abdallah on Wednesday, 11 December 2019.
##


import network
from time import sleep

networkSSID = 'iRobot-Guest'
networkPsswd = ''

# This is a timeout for attempting to connect to a network. We'll wait for networkConTimeout_s
# and "sleep" the system for as long as the "networkTmrInc_s". This way once we reach the total
# networkConTimeout_s duration, we've considered that the network connection timed out.

# network variables are in Seconds.

networkConTimeout_s = 10 
networkTmrInc_s = 0.1

wlan = network.WLAN(network.STA_IF)


class NetworkError(BaseException):
    pass

def isConnected():
    return wlan.isconnected()


def configureNetwork ():
    
    #wlan = network.WLAN(network.STA_IF)
    networkTimer = 0;
    
    wlan.active(True)
    
    if not wlan.isconnected():
        print("connecting to network", networkSSID, networkPsswd)
        wlan.connect(networkSSID, networkPsswd)

    while (not wlan.isconnected() and networkTimer < networkConTimeout_s):
        sleep(networkTmrInc_s)
        networkTimer += networkTmrInc_s
        
    if not wlan.isconnected():
        print("Couldn't connect to the network")
    else:
        print("Network Succesfully Configured.")
        print("network config:", wlan.ifconfig())


