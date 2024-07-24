from tkinter import *
from PIL import ImageTk, Image 


root = Tk()
root.title("Image Viewer")

my_img = ImageTk.PhotoImage(Image.open('images/915592_723423187803629_27414784_n.png'))
my_img1 = ImageTk.PhotoImage(Image.open('images/11358208_866411136766382_1881905483_n.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/11374549_1578408385758151_1193965882_n.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/11374333_486684564840510_197135174_n.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/11184739_829080733846700_362293602_a.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/11363811_1472145896414774_132863191_n.png'))

image_list = [my_img,my_img1,my_img2,my_img3,my_img4,my_img5]


my_label = Label(image=my_img)
my_label.grid(row=0,column=0, columnspan=3)


# btn fn
def backward(n):
	global my_label
	global btn_forward
	global btn_backward
	
	# get rid on present image
	my_label.grid_forget()
	# new img
	my_label = Label(image=image_list[n-1])
	btn_forward = Button(root, text=">>", command=lambda: forward(n+1))
	btn_backward = Button(root, text="<<", command=lambda: backward(n-1))
	# disable forward btn if it reaches last image	
	if n == 1:
		btn_backward = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0,column=0, columnspan=3)
	btn_backward.grid(row=1,column=0)
	btn_forward.grid(row=1,column=2)

def forward(n):
	global my_label
	global btn_forward
	global btn_backward
	
	# get rid on present image
	my_label.grid_forget()
	# new img
	my_label = Label(image=image_list[n-1])
	btn_forward = Button(root, text=">>", command=lambda: forward(n+1))
	btn_backward = Button(root, text="<<", command=lambda: backward(n-1))
	# disable forward btn if it reaches last image	
	if n == 6:
		btn_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0,column=0, columnspan=3)
	btn_backward.grid(row=1,column=0)
	btn_forward.grid(row=1,column=2)
		
		
	
	
	



# previous btn
btn_backward = Button(root, text="<<", command=lambda: backward)
# shuffle btn
btn_quit = Button(root, text="Exit", command=root.quit)
# next btn
btn_forward = Button(root, text=">>", command=lambda: forward(2))

btn_backward.grid(row=1,column=0)
btn_quit.grid(row=1,column=1)
btn_forward.grid(row=1,column=2)























root.mainloop()
