from QuestionDatabase import QuestionDatabase
from Player import Player
from PlayerInputPrompt import PlayerInputPrompt


class GameEngine:
    # class variables here
    MIN_PLAYERS = 1
    MAX_PLAYERS = 3

    inputUtil = PlayerInputPrompt()

    def __init__(self):
        # any instance variables should be declared here
        self.currentPlayersTurn = 0     # keeps track of which players turn it is
        self.players = []   # list of Player objects
        self.db = None  # the database of Question objects


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

    def askQuestion(self):
        pass


# create a game object so we can begin the game
game = GameEngine()
game.begin('database1.xml')
game.getPlayers()

print 'Players'
for i in range(0, len(game.players)):
    print game.players[i].name

# q = game.db.getQuestion(0)
# print q.prompt
