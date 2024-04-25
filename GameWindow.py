import random
import tkinter as tk

import pygame
from tkinter import PhotoImage
from HangmanGame import HangmanGame
from Dictionary import Dictionary
from GameState import GameState

class GameWindow:
    def __init__(self, root):
        self.root = root
        root.title("Word Gallows: The Final Guess")
        #adjusted size to fit all categories
        root.geometry('800x750')
        self.play_sound()
        pygame.init()
      

        # Main Menu
        self.main_menu = tk.Frame(root)
        self.main_menu.pack(fill=tk.BOTH, expand=True)


        # Title Label
        self.title_label = tk.Label(self.main_menu, text='Word Gallows: The Final Guess', font=('Arial', 24, 'bold'))
        self.title_label.pack(pady=(100, 100))

        # Start Button
        self.start_btn = tk.Button(self.main_menu, text='Start', command=self.choose_category, font=('Arial', 20), width=20, pady=20)
        self.start_btn.pack(pady=10)

        # Exit Button
        self.exit_btn = tk.Button(self.main_menu, text='Exit', command=root.quit, font=('Arial', 20), width=20, pady=20)
        self.exit_btn.pack(pady=10)

        
    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("442911__scicodedev__calm_happy_rpgtownbackground.mp3") 
        pygame.mixer.music.play()

    def pause_sound(self):
        pygame.mixer.music.pause()

    def unpause_sound(self):
        pygame.mixer.music.unpause()

    def choose_category(self):
        # hide main frame
        self.main_menu.pack_forget()

        self.choose_category_screen = tk.Frame(self.root)
        self.choose_category_screen.pack(fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.choose_category_screen, text='Choose Category', font=('Arial', 24, 'bold'))
        # self.title_label.pack(pady=(100,50))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(100,50), padx=(60,30))

        self.easy_btn = tk.Button(self.choose_category_screen, text='fruit',  command=lambda: self.choose_difficulty(1), font=('Arial', 20), width=20, pady=15)
        # self.easy_btn.pack(pady=10)
        self.easy_btn.grid(row=1,column=0, padx=(60,10), pady=(10,10))

        self.medium_btn = tk.Button(self.choose_category_screen, text='music',  command=lambda: self.choose_difficulty(2), font=('Arial', 20), width=20, pady=15)
        # self.medium_btn.pack(pady=10)
        self.medium_btn.grid(row=1,column=1, padx=(10,10), pady=(10,10))

        self.hard_btn = tk.Button(self.choose_category_screen, text='literature',   command=lambda: self.choose_difficulty(3), font=('Arial', 20), width=20, pady=15)
        # self.hard_btn.pack(pady=10)
        self.hard_btn.grid(row=2,column=0, padx=(60,10), pady=(10,10))

        self.easy_btn = tk.Button(self.choose_category_screen, text='animals',  command=lambda: self.choose_difficulty(4), font=('Arial', 20), width=20, pady=15)
        # self.easy_btn.pack(pady=10)
        self.easy_btn.grid(row=2,column=1, padx=(10,10), pady=(10,10))

        self.random_number = random.randrange(1,4)
        self.easy_btn = tk.Button(self.choose_category_screen, text='random',  command=lambda: self.choose_difficulty(self.random_number), font=('Arial', 20), width=20, pady=15)
        # self.easy_btn.pack(pady=10)
        self.easy_btn.grid(row=3,column=0,columnspan=2, padx=(60,10), pady=(10,10))



    def choose_difficulty(self, category):
        # hide category frame
        self.choose_category_screen.pack_forget()

        self.choose_difficulty_screen = tk.Frame(self.root)
        self.choose_difficulty_screen.pack(fill=tk.BOTH, expand=True)
        
        # Title Label
        self.title_label = tk.Label(self.choose_difficulty_screen, text='Choose Difficulty', font=('Arial', 24, 'bold'))
        self.title_label.pack(pady=(100, 100))

        # easy, medium, hard difficulty buttons
        # The lambda: just delays execution until the button is pressed. I'm not sure why it immediately executes without this.
        self.easy_btn = tk.Button(self.choose_difficulty_screen, text='easy', command=lambda: self.start_game(category, 1), font=('Arial', 20), width=20, pady=20)
        self.easy_btn.pack(pady=10)

        self.medium_btn = tk.Button(self.choose_difficulty_screen, text='medium', command=lambda: self.start_game(category, 2), font=('Arial', 20), width=20, pady=20)
        self.medium_btn.pack(pady=10)

        self.hard_btn = tk.Button(self.choose_difficulty_screen, text='hard',  command=lambda: self.start_game(category, 3), font=('Arial', 20), width=20, pady=20)
        self.hard_btn.pack(pady=10)

    def start_game(self, category, difficulty):
        # Hide the difficulty selection frame
        self.choose_difficulty_screen.pack_forget()

        # Start the game and choose difficulty
        dictionary = Dictionary()
        dictionary.choose_category_and_difficulty(category, difficulty)
        dictionary.randomization()

        game_state = GameState(dictionary.chosen_word)
        new_frame = HangmanGame(self.root, game_state)
        new_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('')