from QuestionDatabase import QuestionDatabase
from Player import Player
from PlayerInputPrompt import PlayerInputPrompt
from SpinWheel import SpinWheel
import random
import signal, os

def handleSignal(signum, frame):
    print 'signal caught'


class GameEngine:
    # class variables here
    MIN_PLAYERS = 1
    MAX_PLAYERS = 3

    PLAYER_PICK = 6    # sector number which lets the player pick the category
    OPPONENT_PICK = 7    # sector number which lets the player pick the category
    LOSE_TURN = 8    # lose turn sector number
    FREE_TURN = 9    # lose turn sector number
    BANKRUPT = 10    # bankrupt sector number
    RESPIN = 11     # respoint sector number

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

    # prompts a player to pick what category they play
    def pickOwnCategory(self, player):
        prompt = player.name + ', what category would you like to play?\n' + \
            'Enter a number between 1-6\n'
        categoryId = self.inputUtil.promptPlayer(prompt)

        prompt = '\nPlease enter a valid number between 1-6\n' + \
                 'What category would you like to play? '

        # TODO check if there are questions left in the category they choose
        # if their entry is not a number or its outside our limit of 1-3 players
        while not categoryId.isdigit() or \
                (int(categoryId) < 1 or \
                int(categoryId) > 6):
            categoryId = self.inputUtil.promptPlayer(prompt)

        categoryId = int(categoryId)
        return categoryId

    # prompts a player to pick what category their opponent plays
    def pickOpponentCategory(self, player, opponent):
        prompt = opponent.name + ', what category would you like ' + \
            player.name + ' to play?\n' + \
            'Enter a number between 1-6\n'
        categoryId = self.inputUtil.promptPlayer(prompt)

        prompt = '\nPlease enter a valid number between 1-6\n' + \
                 'What category would you like ' + player.name + ' play? '

        # TODO check if there are questions left in the category they choose
        # if their entry is not a number or its outside our limit of 1-3 players
        while not categoryId.isdigit() or \
                (int(categoryId) < 1 or \
                int(categoryId) > 6):
            categoryId = self.inputUtil.promptPlayer(prompt)

        categoryId = int(categoryId)
        return categoryId

    def pickWinner(self):
        winner = None
        for p in self.players:
            if sum(p.points) > 0:
                winner = p
            if winner is not None and sum(p.points) >= sum(winner.points):
                winner = p

        # TODO handle ties, or when there is no score
        if winner is not None:
            print 'Congradulations ' + winner.name + ' you are the winner!'
        else:
            print 'There was no winner this game'

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
        # takes care of doubling the points in round 2
        # would possibly also work
        points = points * self.round


        if correct:
            print 'Correct'
            player.points[self.round-1] = player.points[self.round-1] + points

        elif not correct:
            print 'Incorrect'
            player.points[self.round-1] -= points   

        print player.name + ' now has ' + \
            str(sum(player.points)) + ' points'

    def askQuestion(self, player, categoryId):
        question = self.db.getQuestion(categoryId)
        print 'cat id: ' + str(categoryId)

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

        promptMsg = 'Prompt: ' + question.prompt + '\n' \
            + player.name + '\'s response: '
        keyHints = 'Keys: ' + str(question.keywords)
        print keyHints
        answer = self.inputUtil.promptPlayer(promptMsg)

        correct = self.evaluateAnswer(question, answer)

        # take care of adding/subtracting players score
        self.registerScore(player, correct, question.points)

    def takeTurn(self, player):
        wheelSpot = self.wheel.spin()

        # this is a question sector, ask a question
        if wheelSpot < 5:
            self.askQuestion(player, wheelSpot)
        elif wheelSpot == GameEngine.PLAYER_PICK:
            categoryId = self.pickOwnCategory(player)
            self.askQuestion(player, categoryId)
            pass
        elif wheelSpot == GameEngine.OPPONENT_PICK:
            opponentId = random.randrange(0, len(self.players), 1)
            # players cant pick thier own category here
            while opponentId == player.id:
                opponentId = random.randrange(0, len(self.players), 1)
            categoryId = self.pickOpponentCategory(player, self.players[opponentId])
            self.askQuestion(player, categoryId)
        elif wheelSpot == GameEngine.LOSE_TURN:
            print 'Sorry, you lose this turn'
        elif wheelSpot == GameEngine.FREE_TURN:
            print 'You get a FREE TURN Token!'
            player.freeTurnTokens = player.freeTurnTokens + 1
        elif wheelSpot == GameEngine.BANKRUPT:
            print 'Sorry, you lose your points for this round'
            player.points[self.round-1] = 0
        elif wheelSpot == GameEngine.RESPIN:
            print 'Spin Again!'
            self.takeTurn(player)
        else:
            print 'Error: this sector is not implemented!!!!'


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
print game.db.getRounds()
for rounds in range(0, game.db.getRounds()):
    while game.db.hasQuestions():
        player = game.players[activePlayerId]

        print player.name + '\'s turn'
        game.takeTurn(player)
        activePlayerId = (activePlayerId + 1) % len(game.players)

    game.db.nextRound()
    game.round = game.round + 1

# should move to round 2 here

game.pickWinner()

# q = game.db.getQuestion(0)
# print q.prompt
