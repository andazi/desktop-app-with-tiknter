from tkinter import *


root = Tk()

root.title("Buttons")

myButton = Button(root, text="Click Me!").pack()
# disabled buttons
disabledButton = Button(root, text="Disabled!", state=DISABLED).pack()
# padding
paddedButton = Button(root, text="padded X!", padx=50).pack()
paddedButton = Button(root, text="padded Y", pady=25).pack()

# action
def myClick():
	label = Label(root, text="Oh No!, I got clicked!").pack()
# click
myButton = Button(root, text="Don't Click", padx = 30, pady=15, command = myClick).pack()
























root.mainloop()
