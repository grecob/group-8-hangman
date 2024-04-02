import tkinter as tk
from HangmanGame import HangmanGame
from Dictionary import Dictionary
from GameState import GameState

class GameWindow:
    def __init__(self, root):
        self.root = root
        root.title("Word Gallows: The Final Guess")
        root.geometry('800x650')

        # Main Menu
        self.main_menu = tk.Frame(root)
        self.main_menu.pack(fill=tk.BOTH, expand=True)

        # Title Label
        self.title_label = tk.Label(self.main_menu, text='Word Gallows: The Final Guess', font=('Arial', 24, 'bold'))
        self.title_label.pack(pady=(100, 100))

        # Start Button
        self.start_btn = tk.Button(self.main_menu, text='Start', command=self.choose_difficulty, font=('Arial', 20), width=20, pady=20)
        self.start_btn.pack(pady=10)

        # Exit Button
        self.exit_btn = tk.Button(self.main_menu, text='Exit', command=root.quit, font=('Arial', 20), width=20, pady=20)
        self.exit_btn.pack(pady=10)


    def choose_difficulty(self):
        # hide main frame
        self.main_menu.pack_forget()

        self.choose_difficulty_screen = tk.Frame(self.root)
        self.choose_difficulty_screen.pack(fill=tk.BOTH, expand=True)
        
        # Title Label
        self.title_label = tk.Label(self.choose_difficulty_screen, text='Choose Difficulty', font=('Arial', 24, 'bold'))
        self.title_label.pack(pady=(100, 100))

        # easy, medium, hard difficulty buttons
        # The lambda: just delays execution until the button is pressed. I'm not sure why it immediately executes without this.
        self.easy_btn = tk.Button(self.choose_difficulty_screen, text='easy', command=lambda: self.start_game(1), font=('Arial', 20), width=20, pady=20)
        self.easy_btn.pack(pady=10)

        self.medium_btn = tk.Button(self.choose_difficulty_screen, text='medium', command=lambda: self.start_game(2), font=('Arial', 20), width=20, pady=20)
        self.medium_btn.pack(pady=10)

        self.hard_btn = tk.Button(self.choose_difficulty_screen, text='hard',  command=lambda: self.start_game(3), font=('Arial', 20), width=20, pady=20)
        self.hard_btn.pack(pady=10)

    def start_game(self, difficulty):
        # Hide the difficulty selection frame
        self.choose_difficulty_screen.pack_forget()

        # Start the game and choose difficulty
        dictionary = Dictionary()
        dictionary.choose_difficulty(difficulty)
        dictionary.randomization()

        game_state = GameState(dictionary.chosen_word)
        new_frame = HangmanGame(self.root, game_state)
        new_frame.pack(fill=tk.BOTH, expand=True)