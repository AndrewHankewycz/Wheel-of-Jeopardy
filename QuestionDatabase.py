import xmltodict
from Question import MyQuestion

class QuestionDatabase:
    # class variables here

    def __init__(self):
        # any instance variables should be declared here
        self.category = []    # an array of categories
        pass

    # imports a database of questions from an .xml file
    def importDB(self, filename):
        with open(filename) as fd:
            self.db = xmltodict.parse(fd.read())

        categoryIndex = 0   # categories will be stored by an index in an array
        for cat in self.db['database']['category']:
            self.category.append([])
            catTitle = cat['title']
            # self.category[catTitle] = []

            questions = cat['question'] # an xml question block
            # if there is more than 1 question in this category, (there should be!)
            if type(questions) == list:
                for q in cat['question']:
                    prompt = q['prompt']
                    answer = q['answer']
                    keywords = q['keyword']
                    quest = MyQuestion(catTitle, prompt, answer, keywords)
                    self.category[categoryIndex].append(quest)
            else:
                print 'Error: Only 1 question in this category'

            # when we've imported all the questions from this xml category
            # increment the index and go to the next category
            categoryIndex = categoryIndex + 1

    # returns the next Question object in the category list
    # returns None if none are left in the list, check for this type before using
    def getQuestion(self, category):
        print 'cat: ' + str(category)
        nextQuestion = None
        print(len(self.category))
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
        print count

        return hasQuestions

    def printDB(self):
        print '\nQuestions\n---------'
        for cat in self.category:
            print cat[0].category

            for q in cat:
                print '\t' + q.prompt

# db = QuestionDatabase()
# db.importDB('database1.xml')
# db.printDB()
