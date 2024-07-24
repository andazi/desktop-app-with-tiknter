from tkinter import *
from PIL import ImageTk, Image 


root = Tk()

img = ImageTk.PhotoImage(Image.open("angelo_logo.png"))

my_label = Label(image=img).pack()

btn_quit = Button(root, text="Exit", command=root.quit).pack()



























root.mainloop()








