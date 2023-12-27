from tkinter import *
from tkinter.filedialog import askopenfilenames 
import img2pdf 
root = Tk() 
root.geometry('600x300') 
def select_file(): 
	global file_names 
	file_names = askopenfilenames(initialdir = "/", 
								title = "Select File") 
def image_to_pdf(): 
	for index, file_name in enumerate(file_names): 
		with open(f"file {index}.pdf", "wb") as f: 
			f.write(img2pdf.convert(file_name)) 
def images_to_pdf(): 
	with open(f"file.pdf", "wb") as f: 
		f.write(img2pdf.convert(file_names)) 
Label(root, text = "IMAGE CONVERSION", 
	font = "italic 15 bold").pack(pady = 10) 
Button(root, text = "Select Images", 
	command = select_file, font = 14).pack(pady = 10) 
frame = Frame() 
frame.pack(pady = 20) 
Button(frame, text = "Image to PDF", 
	command = image_to_pdf, 
	relief = "solid", 
	bg = "white", font = 15).pack(side = LEFT, padx = 10) 
Button(frame, text = "Images to PDF", 
	command = images_to_pdf, relief = "solid", 
	bg = "white", font = 15).pack() 
root.mainloop()`  
