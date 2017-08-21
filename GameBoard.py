import sys

class GameBoard:
    # class variables here

    def __init__(self):
        self.categoryTitles = None

    def setDB(self, db):
        self.categoryTitles = []
        for cat in db.category:
            self.categoryTitles.append(cat[0].category)

    def draw(self, db):
        console = sys.stdout    # to save typing

        # print category headings
        for title in self.categoryTitles:
            console.write(' | ' + title)

        print '\n------------------------------'

        catIndex = 1
        for i in range(0, 5, 1):
            for cat in db.category:
                if len(cat) > i:
                    console.write(str(cat[i].points) + '|')
                else:
                    console.write('xxx' + '|')

            print '\n------------------------------'

        # print points section
