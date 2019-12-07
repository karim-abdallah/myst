##
# myst_main.py -- *insert short description* 
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

from machine import Pin
from time import sleep

motor = Pin(2, Pin.OUT)

while True:
    motor.value(not motor.value())
    sleep(0.5)

