import random

class SpinWheel:
    # class variables here

    def __init__(self):
        self.spinCount = 0  # keeps track of the number of spins in the game
        pass


    def spin(self):
        val = random.randrange(0, 12, 1)
        self.spinCount = self.spinCount + 1

        # TODO add graphics here
        
        return val
