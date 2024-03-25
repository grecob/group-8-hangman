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
        self.start_btn = tk.Button(self.main_menu, text='Start', command=self.start_game, font=('Arial', 20), width=20, pady=20)
        self.start_btn.pack(pady=10)

        # Exit Button
        self.exit_btn = tk.Button(self.main_menu, text='Exit', command=root.quit, font=('Arial', 20), width=20, pady=20)
        self.exit_btn.pack(pady=10)

    def start_game(self):
        # Hide the main frame
        self.main_menu.pack_forget()
        
        # Start the game
        dictionary = Dictionary()
        dictionary.choose_category(1)
        dictionary.read_csv()
        game_state = GameState(dictionary.get_chosen_word_instance())
        new_frame = HangmanGame(self.root, game_state)
        new_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameWindow(root)
    root.mainloop()