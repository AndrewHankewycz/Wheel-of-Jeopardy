import sys
import os
from time import sleep

def clearScreen():
    # the unix command
    if os.name == 'posix' or \
        os.name == 'mac' or \
        os.name == 'os2':
        os.system('clear')
    elif os.name == 'nt':
        # the windows command
        os.system('cls')

class WheelUI:
    # class variables here

    def __init__(self):
        self.sectorWords = ['']*12
        self.sectorWords[6] = 'Player Pick'
        self.sectorWords[7] = 'Opponent Pick'
        self.sectorWords[8] = 'Lose Turn'
        self.sectorWords[9] = 'Free Turn'
        self.sectorWords[10] = 'Bankrupt'
        self.sectorWords[11] = 'Respin'

        self.wheelString = ''
        self.sectorIndex = [0] * 12

    # used to store the category titles, since they will disappear once all
    # questions are asked from that category
    def setDB(self, db):
        self.categoryTitles = []
        catIndex = 0
        for cat in db.category:
            self.sectorWords[catIndex] = cat[0].category
            catIndex += 1

        self.generateSectorString()

    def generateSectorString(self):
        self.wheelString = ''

        # append each sector to the string
        i = 0
        for sector in self.sectorWords:
            # console.write(' | ' + sector)
            self.wheelString += ' | ' + sector
            self.sectorIndex[i] = len(self.wheelString) - (len(sector) / 2)
            i += 1
        self.wheelString += ' |'

    def getIndicator(self, pos):
        wheelIndicator = [' '] * len(self.wheelString)
        # for index in self.sectorIndex:
        wheelIndicator[self.sectorIndex[pos]] = '^'

        wheelIndicator = ''.join(wheelIndicator)
        return wheelIndicator

    def animate(self, lastPos, spinPos):
        console = sys.stdout    # to save typing

        line = '  '
        for i in range(0, len(self.wheelString) - 3, 1):
            line += '-'
        line += '  \n'

        failsafe = 0
        i = lastPos # always move forward 1 so it does the animation even if its the same sector
        animations = 1
        while True:
            clearScreen()
            console.write(line)
            # print '  ------------------------------'
            # print category headings
            print self.wheelString
            print self.getIndicator(i % 12)
            # for sector in self.sectorWords:
            #     console.write(' | ' + sector)

            # print '  ------------------------------'
            console.write(line)

            if i % 12 == spinPos and animations > 1:
                break

            animations += 1
            i += 1
            sleep(.25)
