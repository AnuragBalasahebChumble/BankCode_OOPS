import logging
logging.basicConfig(filename='TV.log', level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')


class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # some default list of channels
        self.channelList = [2,4,5,7,9,11,20,36,44,54,65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM


    def power(self):
        self.isOn = not self.isOn    # toggle


    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:  #changing the volume while muted unmutes the sound.
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume -1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # wrap around to the top channel


    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted     # toggle


    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)


    def showInfo(self):
        print()
        logging.info('TV Status: ')
        if self.isOn:
            logging.info("TV is On")
            logging.info(f"Channel is : {self.channelList[self.channelIndex]}")
            if self.isMuted:
                logging.info("sound is muted")
            else:
                logging.info(f"Volume is {self.volume}")
        else:
            logging.info(f"TV is OFF")

# Main code
oTV = TV()   # create the TV object

logging.info("Turn the TV on and show the status")
oTV.power()
oTV.showInfo()

logging.info('the channel up twice, raise the volume twice, show status')

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

logging.info('the TV off, show status, tuen the TV on, show status')

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

logging.info('Lower the volume, mute the sound, show status')

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

logging.info("Change the channel to 11, mute the sound, show the status")
oTV.setChannel(11)
oTV.mute()
oTV.showInfo()