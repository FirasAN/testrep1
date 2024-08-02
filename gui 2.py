# This program displays a window with a title.

from tkinter import *

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = Tk()
        # Display a title.
        self.main_window.title('My First GUI')
        # Enter the tkinter main loop.
        mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()
