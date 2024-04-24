# imports
from GameWindow import GameWindow

import tkinter as tk

# main entry point function
def main():
    root = tk.Tk()
    app = GameWindow(root)
    root.mainloop()

main()