# imports
from Dictionary import Dictionary
from GameState import GameState
from HangmanGame import HangmanGame
import tkinter as tk

# main entry point function
def main():
    # print("please choose a category")
    # print("1. Dictionary")
    # choice = input()
    dictionary = Dictionary()
    # dictionary.choose_category(int(choice))
    dictionary.choose_category(1)
    dictionary.read_csv()

    # create game state object and pass in instance of the chosen word
    game_state = GameState(dictionary.get_chosen_word_instance())

    root = tk.Tk()
    app = HangmanGame(root, game_state)
    root.mainloop()        

main()