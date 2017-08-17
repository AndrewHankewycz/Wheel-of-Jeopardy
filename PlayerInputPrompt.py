

# The benefit of this class is that we can use it for now, define an interface
# for the methods we play to use but later convert this to a GUI if we want
# or just inhance the console behavior

class PlayerInputPrompt:
    # class variables here

    def __init__(self):
        pass

    # presents the player with a text prompt in the console windows
    # returns the player answer as a string
    def promptPlayer(self, prompt):
        playerInput = raw_input(prompt)
        return playerInput
