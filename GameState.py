# keeps track of the game state, such as number of guesses, guessed letters, etc.
import random
class GameState:
    # constructor
    def __init__(self, ChosenWord):
        chosenWord = ChosenWord
        self.secret_word = chosenWord.get_word().lower()
        # print("the secret word is: " + self.secret_word + "\n")

        self.current_word = ''
        
        # set the word that will be shown to underlines
        for letter in self.secret_word:
            self.current_word += '_'
        
        # initialize sets
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.incorrect_word_guesses = set()

        # sets the number of incorrect guesses allowed, put 6 by default for each of the limbs of mr.stickman
        self.allowed_number_of_incorrect = 6
        self.total_number_of_incorrect_guesses = 0

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
    
    def get_incorrect_word_guesses(self):
        return self.incorrect_word_guesses
    
    def get_total_number_of_incorrect_guesses(self):
        return self.total_number_of_incorrect_guesses
    
    def add_incorrect_guess(self):
        self.total_number_of_incorrect_guesses += 1
    
    
    # guess a single letter
    def guess_letter(self, letter):
        # check if user has already guessed this letter
        if(letter.lower() not in self.correct_guesses and letter.lower() not in self.incorrect_guesses):
            # correct guess
            if( letter.lower() in self.secret_word):
                # update the correct_guesses set
                self.correct_guesses.add(letter.lower())
                self.update_current_word(letter.lower())
                return True
            
            # incorrect guess
            else:
                # update the incorrect_guesses set
                self.incorrect_guesses.add(letter.lower())
                self.total_number_of_incorrect_guesses += 1
                return False
    
    
    # guess the whole word
    def guess_word(self, word):
        # word matches, send win sequence - TODO
        if( word.lower() == self.secret_word):
            # print("entire word matches.")
            self.current_word = word.lower()
            return True
        
        # word does not match, draw a part of the hangman - TODO
        else:
            # print("entire word does not match.")
            self.incorrect_word_guesses.add(word.lower())
            self.total_number_of_incorrect_guesses += 1
            # print('num of incorrect guesses: ' + str(self.get_number_of_incorrect_guesses() + self.get_number_of_incorrect_word_guesses()))
            return False
    
    #Provide the hint    
    def get_hint_letter(self):
        hint_letter = ""
        while True:
            hint_letter = random.choice(self.secret_word)
            if hint_letter not in  self.correct_guesses:
                break
        self.correct_guesses.add(hint_letter)
        self.update_current_word(hint_letter)

    def get_current_word(self):
        return self.current_word
    
    def get_secret_word(self):
        return self.secret_word
    
    def get_number_of_unique_letters(self):
        unique_letters = set(self.secret_word)
        return len(unique_letters)
    
    def update_current_word(self, letter):
        # create a list of chars from the current word
        current_word_list = list(self.current_word)
        # loop through the list
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == letter.lower():
                current_word_list[i] = self.secret_word[i]
        # rejoin the list, updating the word 
        self.current_word = ''.join(current_word_list)

    # returns true if the currently guessed word matches the secret word
    def check_win(self):
        if(self.current_word == self.secret_word):
            return True
        else:
            return False
    
    # returns true if the total number of guesses reaches the number allowed, hangman is fully drawn
    def check_lose(self):
        # if(self.allowed_number_of_incorrect == self.get_number_of_incorrect_guesses() + self.get_number_of_incorrect_word_guesses()):
        if(self.allowed_number_of_incorrect == self.total_number_of_incorrect_guesses):
            return True
        else: 
            return False