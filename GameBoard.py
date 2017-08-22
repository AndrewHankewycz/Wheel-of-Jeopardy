import sys

class GameBoard:
    # class variables here

    def __init__(self):
        self.categoryTitles = None

    def setDB(self, db):
        self.categoryTitles = []
        for cat in db.category:
            self.categoryTitles.append(cat[0].category)

    def draw(self, db, curRound):
        console = sys.stdout    # to save typing

        print ' ------------------------------------------------'
        # print category headings
        console.write(' |')
        for title in self.categoryTitles:
            console.write(title + '\t|')

        print '\n ------------------------------------------------'

        catIndex = 1
        for i in range(0, 5, 1):
            console.write(' |')
            for cat in db.category:
                written = False
                for q in cat:
                    if q.points / curRound / 100 == (i + 1):
                        console.write(str(q.points) + '\t|')
                        written = True
                if written == False:
                    console.write('xxx' + '\t|')

            print '\n ------------------------------------------------'

        # print points section
