# DimmerSwitch class

import logging

logging.basicConfig(filename='dimmerSwitch.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevels(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        logging.info(f"Switch is on? : {self.switchIsOn}")
        logging.info(f"Brightness is: {self.brightness}")


oDimmerSwitch1 = DimmerSwitch()
oDimmerSwitch1.show()

