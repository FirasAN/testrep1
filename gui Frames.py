# This program creates labels in two different frames. 

import tkinter
import tkinter.messagebox

class MyGUI:
	def __init__(self):
		# Create the main window widget.
		self.main_window = tkinter.Tk()

		# Create two frames, one for the top of the
		# window, and one for the bottom.
		self.top_frame = tkinter.Frame(self.main_window,borderwidth='4',relief='solid')
		self.bottom_frame = tkinter.Frame(self.main_window,borderwidth='1',relief='solid')

		# Create three Label widgets for the
		# top frame.
		self.label1 = tkinter.Label(self.top_frame,text='Winken')
		self.label2 = tkinter.Label(self.top_frame,text='Blinken')
		self.label3 = tkinter.Label(self.top_frame,text='Nod')
		# Create three Label widgets for the
		# bottom frame.
		self.label4 = tkinter.Label(self.bottom_frame,text='Winken')
		self.label5 = tkinter.Label(self.bottom_frame,text='Blinken')
		self.label6 = tkinter.Label(self.bottom_frame,text='Nod')
		
		#Create Buttons
		self.my_button = tkinter.Button(self.main_window, text='Click me!', command=self.do_something)
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
		
		# Pack the labels that are in the bottom frame.
		# Use the side='left' argument to arrange them
		# horizontally from the left of the frame.
		self.label1.pack()
		self.label2.pack()
		self.label3.pack()
		
		self.label4.pack(side='left')
		self.label5.pack(side='left')
		self.label6.pack(side='left')

		# Yes, we have to pack the frames too!
		self.top_frame.pack()
		self.bottom_frame.pack()
		
		# Pack Buttons
		self.my_button.pack()
		self.quit_button.pack()

		# Enter the tkinter main loop.
		tkinter.mainloop()
	def do_something(self):
		tkinter.messagebox.showinfo('Response', 'My name is Firas')

# Create an instance of the MyGUI class.
if __name__ == '__main__':
	my_gui = MyGUI()
