import tkinter as tk
#class
class HangmanGame:
    

    def __init__(self, root):
        self.root = root
        root.geometry('800x550')
        root.title("Word Gallows: The Final Guess")

        # Create a menubar
        self.menubar = tk.Menu(root)
        root.configure(menu=self.menubar)


        # Create menu
        view_menu = tk.Menu(self.menubar)
        #Help button is drop down menu
        self.menubar.add_cascade(label="Help", menu=view_menu)
         # Add menu items
        view_menu.add_command(label='Pause')
        view_menu.add_command(label='Quit')
        #Settinggs button switches window
        view_menu.add_command(label="Settings", command=self.switch_to_settings)
       

        # label for page display
        self.page_label = tk.Label(root, text="Word Gallows: The Final Guess")
        self.page_label.pack()
        
        #create canvas for hangman
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()
        
        #draw 
        self.canvas.create_line(70, 20, 70, 300, width=2) #vertical
        self.canvas.create_line(70, 20, 150, 20, width=2) #horizontal
        self.canvas.create_line(150, 20, 150, 50, width=2) #noose
        
        
        

    def switch_to_settings(self):
        self.page_label.config(text="Settings Page")
        
       
  

if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()