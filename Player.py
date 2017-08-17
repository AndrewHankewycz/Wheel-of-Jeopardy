
class Player:
    # class variables here

    def __init__(self, id, name):
        # any instance variables should be declared here
        self.id = id     # TODO not sure why players have ids right now
        self.name = name  # players name
        self.round1Points = 0   # point total from round 1
        self.round2Points = 0   # point total from round 2
        self.numOfTokens = 0    # number of take turn tokens
