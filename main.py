# imports
from Dictionary import Dictionary
from GameState import GameState

# main entry point function
def main():
    print("please choose a category")
    print("1. Dictionary")
    choice = input()
    dictionary = Dictionary()
    dictionary.choose_category(int(choice))
    dictionary.read_csv()

    # create game state object and pass in instance of the chosen word
    game_state = GameState(dictionary.get_chosen_word_instance())

    # game loop
    while(True):
        # TODO debug
        print("current word: " + game_state.current_word)
        user_guess = input("Enter your guess (letter or whole word)").lower()
        # letter guessed
        if len(user_guess.strip()) == 1:
            game_state.guess_letter(user_guess)
        # word guessed
        else:
            game_state.guess_word(user_guess)
        

main()