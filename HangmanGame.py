import tkinter as tk
#class
class HangmanGame:
    

    def __init__(self, root, game_state):
        self.root = root
        self.game_state = game_state
        self.incorrect_guesses = []


        root.geometry('800x650')
        root.title("Word Gallows: The Final Guess")

        # Create a menubar
        # self.menubar = tk.Menu(root)
        # root.configure(menu=self.menubar)


        # Create menu
        # view_menu = tk.Menu(self.menubar)
        #Help button is drop down menu
        # self.menubar.add_cascade(label="Help", menu=view_menu)
         # Add menu items
        # view_menu.add_command(label='Pause')
        # view_menu.add_command(label='Quit')
        # #Settinggs button switches window
        # view_menu.add_command(label="Settings", command=self.switch_to_settings)
       

        # label for page display
        self.page_label = tk.Label(root, text="Word Gallows: The Final Guess")
        self.page_label.pack()
        
        #create canvas for hangman
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.display_var = tk.StringVar()
        self.display_label = tk.Label(root, textvariable=self.display_var, font=("Helvetica", 16))
        self.display_label.pack(pady=(0, 20))

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        #draw
        self.canvas.create_line(70, 70, 70, 300, width=2) #vertical
        self.canvas.create_line(70, 70, 150, 70, width=2) #horizontal
        self.canvas.create_line(150, 70, 150, 100, width=2) #noose
        self.canvas.create_line(20, 300, 220, 300, width=2) #base

        self.update_display()
        
    def update_display(self, message=""):
        current_word_display = ' '.join(self.game_state.current_word)
        incorrect_guesses = ', '.join(self.game_state.get_incorrect_guesses())
        incorrect_word_guesses = ', '.join(self.game_state.get_incorrect_word_guesses())
        display_message = f"Guess a letter:\n{current_word_display}"

        if incorrect_guesses:
            display_message += f"\nIncorrect guesses: {incorrect_guesses}"

        if incorrect_word_guesses:
            display_message += f"\nIncorrect words: {incorrect_word_guesses}"

        if message:
            display_message += f"\n{message}"

        self.display_var.set(display_message)

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        end_game_message = ""

        if len(guess) == 1:
            if self.game_state.guess_letter(guess) == False:
                self.draw_next_part(self.game_state.get_total_number_of_incorrect_guesses())
        else:
            if self.game_state.guess_word(guess) == False:
                self.draw_next_part(self.game_state.get_total_number_of_incorrect_guesses())         

        if self.game_state.check_win():
            end_game_message = "Congratulations! You've guessed the word!"
            self.guess_entry.config(state='disabled')
            self.guess_button.config(state='disabled')

        elif self.game_state.check_lose():
            end_game_message = f"You Lose! The word was: {self.game_state.secret_word}"
            self.guess_entry.config(state='disabled')
            self.guess_button.config(state='disabled')

        self.update_display(end_game_message)
    
    def switch_to_settings(self):
        self.page_label.config(text="Settings Page")
        
    def draw_next_part(self, mistakes):
        if mistakes == 1:
            self.canvas.create_oval(130, 100, 170, 140, width=3)  
        elif mistakes == 2:
            self.canvas.create_line(150, 140, 150, 200, width=3)  
        elif mistakes == 3:
            self.canvas.create_line(150, 150, 130, 170, width=3)  
        elif mistakes == 4:
            self.canvas.create_line(150, 150, 170, 170, width=3)  
        elif mistakes == 5:
            self.canvas.create_line(150, 200, 130, 230, width=3)  
        elif mistakes == 6:
            self.canvas.create_line(150, 200, 170, 230, width=3)  

  

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    app.update_display()
    root.mainloop()