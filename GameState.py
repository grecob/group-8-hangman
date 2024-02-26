# keeps track of the game state, such as number of guesses, guessed letters, etc.
import random
class GameState:
    # constructor
    def __init__(self, ChosenWord):
        chosenWord = ChosenWord
        self.secret_word = chosenWord.get_word().lower()
        print("the secret word is: " + self.secret_word + "\n")

        self.current_word = ''
        
        # set the word that will be shown to underlines
        for letter in self.secret_word:
            self.current_word += '_'
        
        # initialize sets
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.incorrect_word_guesses = set()

    # return how many times a correct guess has happened
    def get_number_of_correct_guesses(self):
        return len(self.correct_guesses)
    
    def get_correct_guesses(self):
        return self.correct_guesses
    
    
    # return how many times an incorrect guess has happened
    def get_number_of_incorrect_guesses(self):
        return len(self.incorrect_guesses)
    
    def get_number_of_incorrect_word_guesses(self):
        return len(self.incorrect_word_guesses)
    
    def get_incorrect_guesses(self):
        return self.incorrect_guesses
    
    
    # guess a single letter
    def guess_letter(self, letter):
        # check if user has already guessed this letter
        if(letter.lower() not in self.correct_guesses and letter.lower() not in self.incorrect_guesses):
            # correct guess
            if( letter.lower() in self.secret_word):
                print("correct letter guessed.")
                # update the correct_guesses set
                self.correct_guesses.add(letter.lower())
                self.update_current_word(letter.lower())

                # TODO check win condition
                return True
            
            # incorrect guess
            else:
                # update the incorrect_guesses set
                self.incorrect_guesses.add(letter.lower())
                print("incorrect letter guessed.")
                print("number of incorrect guesses: " + str(self.get_number_of_incorrect_guesses() + self.get_number_of_incorrect_word_guesses()))
                print(self.current_word)
                return False
        else:
            print("letter already guessed")
    
    
    # guess the whole word
    def guess_word(self, word):
        # word matches, send win sequence - TODO
        if( word.lower() == self.secret_word):
            print("entire word matches.")

            return True
        
        # word does not match, draw a part of the hangman - TODO
        else:
            print("entire word does not match.")
            self.incorrect_word_guesses.add(word.lower())
            print('num of incorrect guesses: ' + str(self.get_number_of_incorrect_guesses() + self.get_number_of_incorrect_word_guesses()))
            return False

    def get_current_word(self):
        return self.current_word
    
    def update_current_word(self, letter):
        # create a list of chars from the current word
        current_word_list = list(self.current_word)
        # loop through the list
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == letter.lower():
                current_word_list[i] = self.secret_word[i]
        # rejoin the list, updating the word 
        self.current_word = ''.join(current_word_list)
    
