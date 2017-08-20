
class Player:
    # class variables here

    def __init__(self, id, name):
        # any instance variables should be declared here
        self.id = id     # TODO not sure why players have ids right now
        self.name = name  # players name
        self.points = 0   # points total
        self.numOfTokens = 0    # number of take turn tokens
