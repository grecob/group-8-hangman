import csv
import random
from ChosenWord import ChosenWord
#temp file name
class Dictionary:  
    chosen_word = ChosenWord()
    chosen_category = ''
    random_number = 0
    
    def get_chosen_word_instance(self):
        return self.chosen_word
    
    def choose_category(self, category):
        catalog_of_categories = {
            1: "DictionaryWords.csv"
            #we can add more later
        }
        self.choosen_category = catalog_of_categories.get(category)
        
    
    def randomization(self):
        self.random_number = random.randrange(0, 5)

    def read_csv(self):
        row_number = 0
        self.randomization()
        with open(self.choosen_category, mode ='r')as csv_file:
            heading = next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_file:
                if row_number == self.random_number:
                    line = str(row)
                    split_line = line.split(',')               
                    self.chosen_word.set_word(split_line[0])
                    self.chosen_word.set_hint1(split_line[1])
                    self.chosen_word.set_hint2(split_line[2])
                    self.chosen_word.set_hint3(split_line[3])
                    break
                row_number = row_number + 1