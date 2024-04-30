import random
import tkinter as tk

import pygame
from tkinter import PhotoImage
from HangmanGame import HangmanGame
from Dictionary import Dictionary
from GameState import GameState

#class that inherits tk.label
class BackgroundLabel(tk.Label):
    #constructor method to inherit parent arguments / keyword arguments
    def __init__(self, parent, *args, **kwargs):
        #calls parent class contructor
        super().__init__(parent, *args, **kwargs)
        self.background_image = None

    def set_background_image(self, image_path):
        self.background_image = PhotoImage(file=image_path)
        self.configure(image=self.background_image)


class GameWindow:
    def __init__(self, root):
        self.root = root
        root.title("Word Gallows: The Final Guess")
        root.geometry('800x750')
        root.resizable(False, False)
        self.play_sound()
        self.current_background_label = None
        pygame.init()

         # Main Menu
        self.main_menu = tk.Frame(root)
        self.main_menu.pack(fill=tk.BOTH, expand=True)

        # New background label for main menu (will be created for each)
        self.current_background_label = BackgroundLabel(root)
        self.current_background_label.pack(fill=tk.BOTH, expand=True)
        self.current_background_label.set_background_image("mainmenuimg.png")

        # Title Label
        self.title_label = tk.Label(self.current_background_label, text='Word Gallows: The Final Guess', font=('Arial', 34, 'bold'), bg='gold', fg='white', relief='raised')
        self.title_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Start Button
        self.start_btn = tk.Button(self.current_background_label, text='Start', command=self.choose_category, font=('Arial', 20), width=20, pady=20, bg='skyblue', fg='white', relief='groove')
        self.start_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Exit Button
        self.exit_btn = tk.Button(self.current_background_label, text='Exit', command=root.quit, font=('Arial', 20), width=20, pady=20, bg='skyblue', fg='white', relief='groove')
        self.exit_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("442911__scicodedev__calm_happy_rpgtownbackground.mp3") 
        pygame.mixer.music.play()

    def pause_sound(self):
        pygame.mixer.music.pause()

    def unpause_sound(self):
        pygame.mixer.music.unpause()

    def choose_category(self):
        # Destroy current background label
        if self.current_background_label:
            self.current_background_label.destroy()

        # Create a new background label for choose_category
        self.current_background_label = BackgroundLabel(self.root)
        self.current_background_label.pack(fill=tk.BOTH, expand=True)
        self.current_background_label.set_background_image("fantasy.png")


        self.choose_category_screen = tk.Frame(self.root)
        self.choose_category_screen.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.current_background_label, text='Choose Category', font=('Arial', 30, 'bold'), bg='skyblue', fg='white', relief='groove')
        self.title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.easy_btn = tk.Button(self.current_background_label, text='Fruit',  command=lambda: self.choose_difficulty(1), font=('Arial', 20), width=20, pady=15, bg='skyblue', fg='white', relief='groove')
        self.easy_btn.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

        self.medium_btn = tk.Button(self.current_background_label, text='Music',  command=lambda: self.choose_difficulty(2), font=('Arial', 20), width=20, pady=15, bg='skyblue', fg='white', relief='groove')
        self.medium_btn.place(relx=0.2, rely=0.8, anchor=tk.CENTER)

        self.hard_btn = tk.Button(self.current_background_label, text='Literature',   command=lambda: self.choose_difficulty(3), font=('Arial', 20), width=20, pady=15, bg='skyblue', fg='white', relief='groove')
        self.hard_btn.place(relx=0.8, rely=0.6, anchor=tk.CENTER)

        self.easy_btn = tk.Button(self.current_background_label, text='Animals',  command=lambda: self.choose_difficulty(4), font=('Arial', 20), width=20, pady=15, bg='skyblue', fg='white', relief='groove')
        self.easy_btn.place(relx=0.8, rely=0.8, anchor=tk.CENTER)

        self.random_number = random.randrange(1,4)
        self.easy_btn = tk.Button(self.current_background_label, text='Random',  command=lambda: self.choose_difficulty(self.random_number), font=('Arial', 20), width=20, pady=15, bg='skyblue', fg='white', relief='groove')
        # self.easy_btn.pack(pady=10)
        self.easy_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    
    pass

    def choose_difficulty(self, category):
         # Destroy current background label
        if self.current_background_label:
            self.current_background_label.destroy()

        # Create a new background label for choose_category
        self.current_background_label = BackgroundLabel(self.root)
        self.current_background_label.pack(fill=tk.BOTH, expand=True)
        self.current_background_label.set_background_image("fantasy.png")

        self.choose_difficulty_screen = tk.Frame(self.root)
        self.choose_difficulty_screen.pack(fill=tk.BOTH, expand=True)
        
        # Title Label
        self.title_label = tk.Label(self.current_background_label, text='Choose Difficulty', font=('Arial', 30, 'bold'), bg='skyblue', fg='white', relief='groove')
        self.title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # easy, medium, hard difficulty buttons
        # The lambda: just delays execution until the button is pressed. I'm not sure why it immediately executes without this.
        self.easy_btn = tk.Button(self.current_background_label, text='Easy', command=lambda: self.start_game(category, 1), font=('Arial', 20), width=20, pady=20, bg='skyblue', fg='white', relief='groove')
        self.easy_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.medium_btn = tk.Button(self.current_background_label, text='Medium', command=lambda: self.start_game(category, 2), font=('Arial', 20), width=20, pady=20, bg='skyblue', fg='white', relief='groove')
        self.medium_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.hard_btn = tk.Button(self.current_background_label, text='Hard',  command=lambda: self.start_game(category, 3), font=('Arial', 20), width=20, pady=20, bg='skyblue', fg='white', relief='groove')
        self.hard_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    pass

    def start_game(self, category, difficulty):
        # Destroy current background label
        if self.current_background_label:
            self.current_background_label.destroy()

        # Start the game and choose difficulty
        dictionary = Dictionary()
        dictionary.choose_category_and_difficulty(category, difficulty)
        dictionary.randomization()

        game_state = GameState(dictionary.chosen_word)
        new_frame = HangmanGame(self.root, game_state)
        new_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('')