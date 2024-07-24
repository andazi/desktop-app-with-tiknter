from tkinter import *

root = Tk()

myLabel = Label(root, text="Inputs are called Entry in tkinter").pack()

name = Entry(root)
name.pack()

# default value for name entry
name.insert(0, "Andazi")

def getName():
	greeting = "My name is " + name.get()
	myName = Label(root, text=greeting).pack()
	
myButton = Button(root, text="Enter your Name", padx=25, pady=10, bg='#999', fg='#d4d4d5', command=getName).pack()
























root.mainloop()
