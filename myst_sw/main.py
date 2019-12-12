##
# myst_main.py -- Where it all begins...
#
# On a less glamorous note, this file was renaimed main.py on December 2019 for
# compatibility with micropython. Will revisit this once we scale up.
#
# Written by Karim Abdallah on Saturday,  7 December 2019.
#/

from time import sleep

from initialize import *
from pump import *
from connectivity import *

squirtDuration = 5 # How long should the pump squirt for


def main():

    configureNetwork()
    initializePump()
    initializeChirp()

    while True:
        squirt(squirtDuration)

if __name__ == "__main__":

    main()





