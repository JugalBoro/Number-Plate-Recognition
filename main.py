import tkinter as tk

# Top level window

from tkinter import *
from PIL import Image
import pytesseract
import sys
import PIL
import os.path
from tkinter import *

# Following will import tkinter.ttk module and
# automatically override all the widgets
# which are present in tkinter module.
from tkinter.ttk import *



def GUI():
    im = PIL.Image.open(r"C:\Users\jboro\OneDrive\Desktop\tesseract-python-master\dist\test88.png")

    text = pytesseract.image_to_string(im, lang='eng')

    directory = r'C:\Users\jboro\OneDrive\Desktop\tesseract-python-master\criminal number\criminal_number'

    filename = "Day21March" + ".txt"
    file_path = os.path.join(directory, filename)
    if not os.path.isdir(directory):
        os.mkdir(directory)

    file = open(file_path, "a")
    file.write(text)
    file.close()

    # print(str(i) + ". " + text)
    print(text)
im = PIL.Image.open("test88.png")
text1 = pytesseract.image_to_string(im, lang='eng')

def run():
    text1 = pytesseract.image_to_string(im, lang='eng')
    print(text1)
frame = tk.Tk()
frame.title("Do you want in txt file ?")
frame.geometry('400x200')
# Function for getting Input
# from textbox and printing it
# at label widget




def printInput(text1):
    impp=text1
	#inp = inputtxt.get(text1, text1)
	#lbl.config(text = text1)

# TextBox Creation
#inputtxt = tk.Text(frame,
				#height = 5,
				#width = 20,)
#inputtxt.pack()


# Button Creation
printButton = tk.Button(frame,
						text = "OK",
						command = GUI)



printButton.pack()


# Label Creation
lbl = tk.Label(frame, text = text1)
lbl.pack()
frame.mainloop()




