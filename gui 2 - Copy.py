# This program displays a window with a title.

from tkinter import *

class MyGUI:
	def __init__(self):
		# Create the main window widget.
		self.main_window = Tk()
		# Display a title.
		self.main_window.title('My First GUI')
		
		# Create widgets
		self.label1 = Label(self.main_window,text='Hello World!',borderwidth='4',relief='solid')
		self.label2 = Label(self.main_window,text='This is my GUI program.',borderwidth='4',relief='raised')
		
		
		
		# Call widgets pack method
		#self.label1.pack()
		#self.label2.pack()
		self.label1.pack(side='left', ipadx=20, ipady=20, padx=30, pady=30)
		self.label2.pack(side='right', ipadx=20, ipady=20, padx=30, pady=30)
		
		

		# Enter the tkinter main loop.
		mainloop()

# Create an instance of the MyGUI class.
#my_gui = MyGUI()
if __name__ == '__main__':
	my_gui = MyGUI()