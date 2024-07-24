from tkinter import *

root = Tk()
# grid system is better for positioning widget on screen
# grid starts from 0

myLabel = Label(root, text="Hello World!")
myFocus = Label(root, text="Hello Tkinter")
myName = Label(root, text="Hello Andazi")
myGrace = Label(root, text="Happy Day")

# grid
# grid is trelative
myLabel.grid(row=0,column=0)
myFocus.grid(row=1,column=1)
myName.grid(row=2,column=2)
myGrace.grid(row=0, column=2)

# we can do it in one step since python is object oriented
myMood = Label(root, text="Oh Happy Day").grid(row=2,column=0)








root.mainloop()
























