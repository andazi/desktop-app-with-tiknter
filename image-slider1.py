from tkinter import *
from PIL import ImageTk, Image 


root = Tk()
root.title("Image Viewer")

x = root.winfo_screenwidth() // 2 - 250 # center of the screen
y = int(root.winfo_screenheight() * 0.1) # 10% away from the top
# this create a fixed window size
root.geometry("500x600+" + str(x) + "+" + str(y))


my_img = ImageTk.PhotoImage(Image.open('images/915592_723423187803629_27414784_n.png'))

img = Label(image=my_img)
img.grid(row=0,column=0, columnspan=3)


def backward():
	pass
def shuffle():
	pass
def forward():
	pass



# previous btn
btn_backward = Button(root, text="<<", command=lambda: backward())
btn_backward.grid(row=1,column=0)
# shuffle btn
btn_shuffle = Button(root, text="shuffle", command=lambda: shuffle_img)
btn_shuffle.grid(row=1,column=1)
# next btn
btn_forward = Button(root, text=">>", command=lambda: forward())
btn_forward.grid(row=1,column=2)
















root.mainloop()
