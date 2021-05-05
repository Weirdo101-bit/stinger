import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog,messagebox

window=tk.Tk()
window.title("Stinger")

#Def
version=1.0

####################
def file():
 f_name=name.get()
 file = open(f_name+".txt", "w")
 file.write("Made By W31RD0") 
 file.close() 


def ico():
	global file
	window.filename=filedialog.askopenfilename(initialdir="~/Pictures/icons",title="Select an Icon: ", filetypes=(("png files", "*.png"), ("icon files","*.jpg")))
	icon=ImageTk.PhotoImage(Image.open(window.filename))
	icon.image=icon
	show_ico=Label(image=icon,width="30px",height="30px",bg="white")
	show_ico.grid(row=1, column=3,sticky=E)

window.title("Stinger")
window.configure(bg="white")

#Labels

Label (window,text=version,bg="white", fg="green") .grid (row=0,column=0,sticky=W)
Label (window,text="File name",bg="white", fg="black", font="3px,bold") .grid (row=1,column=0,sticky=E)

#Enters

name=Entry (window, width=10, bg="white",fg="black")
name.grid (row=1, column=1, sticky=E)

#Buttons
Button (window, text="Exit", command=window.destroy, width=4, bg="red",fg="black") .grid (row=6, column=6, sticky=W)
Button (window, text="Generate",command=file,width=8, bg="gray",fg="black") .grid (row=6, column=5, sticky=W)
file=Button (window, text="Ico",command=ico,width=9,bg="gray",fg="black") 
file.grid (row=6, column=4, sticky=W)
 

#mainloop
window.mainloop()