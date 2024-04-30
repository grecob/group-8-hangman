import tkinter as tk
import pygame
import os
#class
class HangmanGame(tk.Frame):    

    def __init__(self, parent, game_state):
        super().__init__(parent)
        self.parent = parent
        self.game_state = game_state
        self.incorrect_guesses = []
        self.play_sound()


        self.canvas_color = 'white'
        self.parent_color = 'white'
        self.letter_color = 'black'
        self.line_color = 'black'
        self.button_color = 'white'
        self.drawings = []

        parent.configure(bg=self.parent_color)

        # Create a menubar
        self.menubar = tk.Menu(parent)
        parent.configure(menu=self.menubar)

        # Create menu
        view_menu = tk.Menu(self.menubar)
        #Help button is drop down menu
        self.menubar.add_cascade(label="Menu", menu=view_menu)
         # Add menu items
        view_menu.add_command(label='Pause', command = self.pause_popup)
        view_menu.add_command(label='Colors', command = self.color_change)
        view_menu.add_command(label = 'Restart', command = self.return_to_main)
        view_menu.add_command(label='Quit', command = self.quit)

        #create canvas for hangman
        self.canvas = tk.Canvas(parent, width=600, height=400, bg=self.canvas_color)
        self.canvas.pack(pady=20)
        
        #add background image
        self.background_image = tk.PhotoImage(file="bg_img.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)


        #Create hint button
        self.dragon_helper = tk.PhotoImage(file="dragon_helper.png")
        self.hint_button = tk.Button(parent, text="Need a hint?", image=self.dragon_helper, compound="bottom", command=self.get_hint)
        self.hint_button.config(width=70, height = 80)
        self.hint_button.pack(side=tk.RIGHT, padx=(0,40))


        self.display_var = tk.StringVar()
        self.display_label = tk.Label(parent, textvariable=self.display_var, font=("Helvetica", 16), fg=self.letter_color, bg=self.parent_color)
        self.display_label.pack(pady=(0, 20))

        self.guess_entry = tk.Entry(parent)
        self.guess_entry.pack()

        self.guess_button = tk.Button(parent, text="Guess", command=self.check_guess, fg=self.letter_color, bg=self.button_color)
        self.guess_button.pack(pady=5)


         #Create sound button
        self.sound_icon = tk.PhotoImage(file="sound_on.png") 
        self.toggle_button = tk.Button(parent, image=self.sound_icon, command=self.toggle_sound, bg=self.parent_color, bd=0)
        self.toggle_button.pack(side=tk.LEFT, padx=(0, 40))

        #draw
        self.drawings.append(self.canvas.create_line(250, 70, 250, 300, width=2, fill=self.line_color)) #vertical
        self.drawings.append(self.canvas.create_line(250, 70, 330, 70, width=2, fill=self.line_color)) #horizontal
        self.drawings.append(self.canvas.create_line(330, 70, 330, 100, width=2, fill=self.line_color)) #noose
        self.drawings.append(self.canvas.create_line(200, 300, 400, 300, width=2, fill=self.line_color)) #base

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

   #sound button
    def play_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("442911__scicodedev__calm_happy_rpgtownbackground.mp3") 
        pygame.mixer.music.play()

    def toggle_sound(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

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

    def get_hint(self):
        if ((self.game_state.get_total_number_of_incorrect_guesses() < 5) and ((self.game_state.get_number_of_correct_guesses() + 1) < self.game_state.get_number_of_unique_letters())):
            self.game_state.add_incorrect_guess()
            self.draw_next_part(self.game_state.get_total_number_of_incorrect_guesses())
            self.game_state.get_hint_letter()
            self.update_display()
            if ((self.game_state.get_total_number_of_incorrect_guesses() >= 5) or ((self.game_state.get_number_of_correct_guesses() + 1) >= self.game_state.get_number_of_unique_letters())):
                self.hint_button.config(text="Sorry!")
                self.hint_button.config(state='disabled')
    
    def switch_to_settings(self):
        self.page_label.config(text="Settings Page")
        
    def draw_next_part(self, mistakes):
        if mistakes == 1:
            self.drawings.append(self.canvas.create_oval(310, 100, 350, 140, width=3, outline=self.line_color))  
        elif mistakes == 2:
            self.drawings.append(self.canvas.create_line(330, 140, 330, 200, width=3, fill=self.line_color))  
        elif mistakes == 3:
            self.drawings.append(self.canvas.create_line(330, 150, 310, 170, width=3, fill=self.line_color))  
        elif mistakes == 4:
            self.drawings.append(self.canvas.create_line(330, 150, 350, 170, width=3, fill=self.line_color))  
        elif mistakes == 5:
            self.drawings.append(self.canvas.create_line(330, 200, 310, 230, width=3, fill=self.line_color))  
        elif mistakes == 6:
            self.drawings.append(self.canvas.create_line(330, 200, 350, 230, width=3, fill=self.line_color))

    def pause_popup(self):
        pauseWindow = tk.Toplevel()
        pauseWindow.grab_set()
        pauseWindow.overrideredirect(True)
        self_x = self.winfo_rootx()
        self_y = self.winfo_rooty()
    # add offset
        win_x = self_x + 325
        win_y = self_y - 300
    # set toplevel in new position
        pauseWindow.geometry(f'200x150+{win_x}+{win_y}') 
        pButton = tk.Button(pauseWindow, text = "unpause", command = pauseWindow.destroy).pack(side="top",pady=60)

    def color_change(self):
        # Function to handle button click
        def on_button_click(color):
            if color == "Purple":
                self.canvas_color = 'white'
                self.parent_color = 'purple'
                self.letter_color = 'black'
                self.line_color = 'black'
                self.button_color = 'white'
            if color == "White":
                self.canvas_color = 'white'
                self.parent_color = 'white'
                self.letter_color = 'black'
                self.line_color = 'black'
                self.button_color = 'white'
            if color == "Black":
                self.canvas_color = 'white'
                self.parent_color = 'black'
                self.letter_color = 'white'
                self.line_color = 'black'
                self.button_color = 'white'
            if color == "Dark Grey":
                self.canvas_color = 'Black'
                self.parent_color = 'dark grey'
                self.letter_color = 'white'
                self.line_color = 'white'
                self.button_color = 'black'
            if color == "Red":
                self.canvas_color = 'white'
                self.parent_color = 'red'
                self.letter_color = 'black'
                self.line_color = 'black'
                self.button_color = 'white'
            if color == "Blue":
                self.canvas_color = 'white'
                self.parent_color = 'blue'
                self.letter_color = 'black'
                self.line_color = 'black'
                self.button_color = 'white'

            update_colors()
            popup.destroy()

        

        def update_colors():
            self.canvas.configure(bg=self.canvas_color)
            self.parent.configure(bg=self.parent_color)
            self.display_label.configure(fg=self.letter_color, bg=self.parent_color)
            self.guess_button.configure(fg=self.letter_color, bg=self.button_color)
            # Change the color of each item
            for i, item in enumerate(self.drawings):
                if i == 4:
                    self.canvas.itemconfig(item, outline=self.line_color)
                else:
                    self.canvas.itemconfig(item, fill=self.line_color)


        # Create popup window
        popup = tk.Toplevel()
        popup.title("Choose a Color")
        
        self_x = self.winfo_rootx()
        self_y = self.winfo_rooty()
        win_x = self_x + 325
        win_y = self_y - 300

        # popup.geometry(f'200x150+{win_x}+{win_y}')  # Set a fixed size for the popup
        
        # Define colors and create buttons
        colors = ["White", "Black", "Dark Grey", "Red", "Purple", "Blue"]
        for color in colors:
            button = tk.Button(popup, text=color, bg=color, 
                            command=lambda c=color: on_button_click(c))
            button.pack(fill='x', padx=10, pady=5)
        

       

    def return_to_main(self):
        self.quit()
        os.startfile("main.py")


  

if __name__ == "__main__":
    parent = tk.Tk()
    app = HangmanGame(parent)
    app.update_display()
    parent.mainloop()