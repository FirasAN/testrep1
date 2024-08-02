# Kilometers to Miles Converter

import tkinter

class KmToMilesConverterGUI:
	def __init__(self):
		# Create the main window widget.
		self.main_window = tkinter.Tk()
		# Display a title.
		self.main_window.title('Kilometers to Miles Converter')

		#Create 3 frames to group widgets
		self.top_frame = tkinter.Frame()
		self.mid_frame = tkinter.Frame()
		self.bottom_frame = tkinter.Frame()
		
		#Create Widges for top_frame
		self.prompt_label = tkinter.Label(self.top_frame,text='Enter a distance in Kilometers:')
		self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
		#Pack top_frame widges
		self.prompt_label.pack(side='left')
		self.kilo_entry.pack(side='left')
		
		#Create Widges for mid_frame
		self.descr_label = tkinter.Label(self.mid_frame,text='Converted to Miles:')
		self.value = tkinter.StringVar()	#Create a StringVar object
		self.miles_label = tkinter.Label(self.mid_frame,textvariable=self.value)	#Associate the StringVar object with the output label
		#Pack mid_frame widges
		self.descr_label.pack(side='left')
		self.miles_label.pack(side='left')
		
		#Create Widges for bottom_frame
		self.calc_button = tkinter.Button(self.bottom_frame,text='Convert',command=self.convert)
		self.quit_button = tkinter.Button(self.bottom_frame,text='Quit',command=self.main_window.destroy)
		#Pack bottom_frame widges
		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')
		
		#Pack the FRAMES
		self.top_frame.pack(ipadx=20, ipady=20, padx=30, pady=30)
		self.mid_frame.pack(ipadx=20, ipady=20, padx=30, pady=30)
		self.bottom_frame.pack(ipadx=20, ipady=20, padx=30, pady=30)
		
		# Enter the tkinter main loop.
		tkinter.mainloop()
		
	def convert(self):
		kilo = float(self.kilo_entry.get())
		miles = kilo * 0.6214
		self.value.set(miles)
		
		#tkinter.messagebox.showinfo('Response', 'Done!')

# Create an instance of the KmToMilesConverterGUI class.
if __name__ == '__main__':
	my_gui = KmToMilesConverterGUI()
