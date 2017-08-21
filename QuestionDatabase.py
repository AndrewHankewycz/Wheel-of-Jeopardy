import xmltodict
from Question import MyQuestion

class QuestionDatabase:
    # class variables here

    def __init__(self):
        # any instance variables should be declared here
        self.rounds = [] # a list to store rounds of questions
        self.category = []    # an array of categories
        pass

    # imports a database of questions from an .xml file
    def importDB(self, filename):
        with open(filename) as fd:
            self.db = xmltodict.parse(fd.read())

        rounds = self.db['database']['round']
        for gameRound in rounds:
            categoryIndex = 0   # categories will be stored by an index in an array

            # make new array so importing rounds wont combine into one list
            self.category = []
            # TODO should probably check that there are enough categories/questions to play a game
            for cat in gameRound['category']:
            # for cat in self.db['database']['round']['category']:
                self.category.append([])
                catTitle = cat['title']
                # self.category[catTitle] = []

                questions = cat['question'] # an xml question block
                # if there is more than 1 question in this category, (there should be!)
                if type(questions) == list:
                    qIndex = 1  # used for calculating how many pts each Q is
                    for q in cat['question']:
                        prompt = q['prompt']
                        answer = q['answer']
                        keywords = q['keyword']
                        points = qIndex * 100
                        quest = MyQuestion(catTitle, prompt, answer, keywords, points)
                        self.category[categoryIndex].append(quest)
                        qIndex = qIndex + 1
                else:
                    print 'Error: Only 1 question in this category'

                # when we've imported all the questions from this xml category
                # increment the index and go to the next category
                categoryIndex = categoryIndex + 1

            # add this round to the list of rounds
            self.rounds.append(self.category)

        # take the first one just becuase
        self.category = self.rounds[0]

    # returns the next Question object in the category list
    # returns None if none are left in the list, check for this type before using
    def getQuestion(self, category):
        nextQuestion = None
        # if this category still has questions
        if len(self.category[category]) > 0:
            nextQuestion = self.category[category][0]   # return the next question in the list
            self.category[category].remove(nextQuestion)

        return nextQuestion

    # checks the categories to see if there are still any questions left
    # returns true if there are still questions
    def hasQuestions(self):
        hasQuestions = False

        count = []
        for cat in self.category:
            count.append(len(cat))
            # if the category array is not empty we still have questions
            if len(cat) > 0:
                hasQuestions = True
        # print count

        if not hasQuestions:
            self.rounds.remove(self.rounds[0])

        return hasQuestions

    # if there is another round in the database, get the questions ready
    def nextRound(self):
        if self.rounds:
            self.category = self.rounds[0]

    # returns the number of rounds in the database
    def getRounds(self):
        return len(self.rounds)

    def printDB(self):
        print '\nQuestions\n---------'
        for cat in self.category:
            print cat[0].category

            for q in cat:
                print '\t' + q.prompt

# db = QuestionDatabase()
# db.importDB('database1.xml')
# db.printDB()
