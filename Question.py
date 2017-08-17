
class MyQuestion:
    # class variables here

    def __init__(self, cat, prompt, answer, keywords):
        # any instance variables should be declared here
        self.category = cat  # category title, not sure why we have this
        self.prompt = prompt    # the prompt the player will be given
        self.answer = answer    # the literal answer, where keywords are taken from
        self.keywords = keywords  # list of keywords that are needed for an accepted answer
