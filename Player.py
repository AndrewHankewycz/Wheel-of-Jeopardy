
class Player:
    # class variables here

    def __init__(self, id, name):
        # any instance variables should be declared here
        self.id = id     # TODO not sure why players have ids right now
        self.name = name  # players name
        self.points = [0,0]   # points total
        self.freeTurnTokens = 0    # number of take turn tokens
    def showScore(self):
        print ' Player ' + self.name + ', round 1 score: ' + str(self.points[0])
        print ' Player ' + self.name + ', round 2 score: ' + str(self.points[1])

