import random
from ChosenWord import ChosenWord
from Words import Words as words
#temp file name
class Dictionary:

    def __init__(self):
        self.chosen_word = ChosenWord()
        self.chosen_difficulty = ""
        self.catalog_of_difficulties = {}
    

    def choose_difficulty(self, difficulty):
        catalog_of_difficulties = {
            1: "easy",
            2: "medium",
            3: "hard"
        }
        self.chosen_difficulty = catalog_of_difficulties[difficulty]
    
    def randomization(self):
        if self.chosen_difficulty == "easy":
            self.random_number = random.randrange(0, len(words.easy))
            self.chosen_word.set_word(words.easy[self.random_number])

        elif self.chosen_difficulty == "medium":
            self.random_number = random.randrange(0, len(words.medium))
            self.chosen_word.set_word(words.medium[self.random_number])

        elif self.chosen_difficulty == "hard":
            self.random_number = random.randrange(0, len(words.hard))
            self.chosen_word.set_word(words.hard[self.random_number])