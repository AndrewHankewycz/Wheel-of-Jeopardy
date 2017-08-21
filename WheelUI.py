import sys

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

    # used to store the category titles, since they will disappear once all
    # questions are asked from that category
    def setDB(self, db):
        self.categoryTitles = []
        catIndex = 0
        for cat in db.category:
            self.sectorWords[catIndex] = cat[0].category
            catIndex += 1

        self.generateString()

    def generateString(self):
        self.wheelString = ''
        self.sectorIndex = [0] * 12

        # append each sector to the string
        i = 0
        for sector in self.sectorWords:
            # console.write(' | ' + sector)
            self.wheelString += ' | ' + sector
            self.sectorIndex[i] = len(self.wheelString) - (len(sector) / 2)
            i += 1
        self.wheelString += ' |'

        self.wheelIndicator = [' '] * len(self.wheelString)
        for index in self.sectorIndex:
            self.wheelIndicator[index] = '^'

        self.wheelIndicator = ''.join(self.wheelIndicator)

    def draw(self, lastPos, spinPos):
        console = sys.stdout    # to save typing

        line = '  '
        for i in range(0, len(self.wheelString) - 3, 1):
            line += '-'
        line += '  \n'
        console.write(line)
        # print '  ------------------------------'
        # print category headings
        print self.wheelString
        print self.wheelIndicator
        # for sector in self.sectorWords:
        #     console.write(' | ' + sector)

        # print '  ------------------------------'
        console.write(line)
