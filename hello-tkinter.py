from tkinter import *
from tkinter import ttk


# everything in tkinter is a widget
# window widget
root = tk.Tk()

# label widget

# to create a thing, we need to define then send to screen
# define
myLabel = Label(root, text="Hello World!")
# send to screen
myLabel.pack()

myFocus = Label(root, text="Hello Tkinter")
myFocus.pack()

myName = tk.Label(root, text="Hello Andazi")
myName.pack()


# create an event loop
# program only ends when the loop ends
root.mainloop()
































