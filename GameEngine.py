from QuestionDatabase import QuestionDatabase
from Player import Player
from PlayerInputPrompt import PlayerInputPrompt
from SpinWheel import SpinWheel


class GameEngine:
    # class variables here
    MIN_PLAYERS = 1
    MAX_PLAYERS = 3

    inputUtil = PlayerInputPrompt()
    wheel = SpinWheel()

    def __init__(self):
        # any instance variables should be declared here
        self.currentPlayersTurn = 0     # keeps track of which players turn it is
        self.players = []   # list of Player objects
        self.db = None  # the database of Question objects
        self.round = 1  # indicates the round number, makes more than 2 rounds possible


    def begin(self, dbFilename):
        print 'Game Beginning'

        self.db = QuestionDatabase()
        self.db.importDB(dbFilename)

        print 'Database imported...'

    def getPlayerName(self, playerNumber):
        prompt = 'Please enter player ' + str(playerNumber + 1) + '\'s name: '
        playerName = self.inputUtil.promptPlayer(prompt)

        prompt = '\nPlease enter a valid name\nPlease enter player ' + \
            str(playerNumber + 1) + '\'s name: '

        # if they dont enter a value at all, its empty prompt again
        while not len(playerName) > 0:
            playerName = self.inputUtil.promptPlayer(prompt)

        return playerName

    def getPlayers(self):
        prompt = 'How many players would you like? '
        numPlayers = self.inputUtil.promptPlayer(prompt)

        prompt = '\nPlease enter a valid number between 1-3\n' + \
                 'How many players would you like? '

        # if their entry is not a number or its outside our limit of 1-3 players
        while not numPlayers.isdigit() or \
                (int(numPlayers) < self.MIN_PLAYERS or \
                int(numPlayers) > self.MAX_PLAYERS):
            numPlayers = self.inputUtil.promptPlayer(prompt)

        numPlayers = int(numPlayers)

        for i in range(0, numPlayers):
            name = self.getPlayerName(i)
            player = Player(i, name)
            self.players.append(player)

    # returns true if the user's answer was correct
    def evaluateAnswer(self, question, answer):
        splitAns = answer.split(' ')

        for word in question.keywords:
            if word in splitAns:
                return True

        return False

    # adds or subtracts points from a players score
    # i dont think we take points away but if we do this will make it nicer
    def registerScore(self, player, correct, points):
        if not correct:
            print 'Incorrect'
            return

        # takes care of doubling the points in round 2
        # would possibly also work
        points = points * self.round

        player.points = player.points + points

        print 'Correct! ' + player.name + ' now has ' + \
            str(player.points) + ' points'

    def takeTurn(self, player):
        print '\nPlayer ' + str(player.id) + '\'s turn'
        wheelSpot = self.wheel.spin()

        # this is a question sector, ask a question
        if wheelSpot < 5:
            question = self.db.getQuestion(wheelSpot)

            # TODO this needs work, if they spin again they could land on a token
            # TODO this needs work, if they spin again they could land on a token
            # TODO this needs work, if they spin again they could land on a token
            # TODO this needs work, if they spin again they could land on a token
            # if there is no question left in this category spin again
            while question is None:
                wheelSpot = self.wheel.spin()
                print 'respinning: ' + str(wheelSpot)
                if wheelSpot < 5:
                    question = self.db.getQuestion(wheelSpot)

            print '\nCategory \'' + question.category + '\''

            promptMsg = 'Prompt: ' + question.prompt + '\nResponse: '
            keyHints = 'Keys: ' + str(question.keywords)
            print keyHints
            answer = self.inputUtil.promptPlayer(promptMsg)

            correct = self.evaluateAnswer(question, answer)

            # take care of adding/subtracting players score
            self.registerScore(player, correct, question.points)
        else:
            # do stuff for other sectors on the board
            # TODO fill this in wiht token stuff
            print 'not a question sector'


# create a game object so we can begin the game
game = GameEngine()
game.begin('database1.xml')


# !!!!!---- test functionality begins here -----!!!!!!

# ---------- begin player input -----------

game.getPlayers()
#
# print 'Players'
# for i in range(0, len(game.players)):
#     print game.players[i].name

# ---------- end player input -----------

activePlayerId = 0
while game.db.hasQuestions():
    player = game.players[activePlayerId]
    game.takeTurn(player)
    activePlayerId = (activePlayerId + 1) % len(game.players)

# q = game.db.getQuestion(0)
# print q.prompt
