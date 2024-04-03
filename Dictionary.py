import random
from ChosenWord import ChosenWord
from Words import Words as words
#temp file name
class Dictionary:

    def __init__(self):
        self.chosen_word = ChosenWord()
        self.chosen_category = ""
        self.chosen_difficulty = ""
        self.catalog_of_difficulties = {}
    

    def choose_category_and_difficulty(self, category, difficulty):
        catalog_of_category = {
            1: "fruit",
            2: "music",
            3: "literature",
            4: "animals"
        }
        catalog_of_difficulties = {
            1: "easy",
            2: "medium",
            3: "hard"
        }
        self.chosen_category = catalog_of_category[category]
        self.chosen_difficulty = catalog_of_difficulties[difficulty]
    
    def randomization(self):
        if self.chosen_category == "fruit" :
            self.random_number = random.randrange(0, len(words.fruit[self.chosen_difficulty]))
            self.chosen_word.set_word(words.fruit[self.chosen_difficulty][self.random_number])

        elif self.chosen_category == "music" :
            self.random_number = random.randrange(0, len(words.music[self.chosen_difficulty]))
            self.chosen_word.set_word(words.music[self.chosen_difficulty][self.random_number])

        elif self.chosen_category == "literature" :
            self.random_number = random.randrange(0, len(words.literature[self.chosen_difficulty]))
            self.chosen_word.set_word(words.literature[self.chosen_difficulty][self.random_number])

        elif self.chosen_category == "animals" :
            self.random_number = random.randrange(0, len(words.animals[self.chosen_difficulty]))
            self.chosen_word.set_word(words.animals[self.chosen_difficulty][self.random_number])