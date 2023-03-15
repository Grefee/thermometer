import readTermMeterList as R
import time
import logging
import conDbTest as X
import idOfTeplomerFromDb as P


class Main:
    timeDelay = open("delay.txt", "r")
    global delay
    delay = int(timeDelay.read())
    def __init__(self):
        R.readTermMeter()
        X.checkTermMetersInDb(R.termListFromXml)
        P.getIdOfTeplomer(R.termListFromXml)



        while True:
            for item in R.termListFromXml:
                P.sendDataToDb(item)
            time.sleep(delay)

## without gui with bad logging
if __name__ == '__main__':
    while True:
        Main()





