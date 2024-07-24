from tkinter import *
from PIL import ImageTk, Image 
import time


root = Tk()
# title
root.title("still not working")



my_img = ImageTk.PhotoImage(Image.open('images/915592_723423187803629_27414784_n.png'))
my_img1 = ImageTk.PhotoImage(Image.open('images/11358208_866411136766382_1881905483_n.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/11374549_1578408385758151_1193965882_n.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/11374333_486684564840510_197135174_n.png'))
my_img4 = ImageTk.PhotoImage(Image.open('images/11184739_829080733846700_362293602_a.png'))
my_img5 = ImageTk.PhotoImage(Image.open('images/11363811_1472145896414774_132863191_n.png'))

image_list = [my_img,my_img1,my_img2,my_img3,my_img4,my_img5]

n = 0
DELAY = 1

for i in range(2):
	# add new image
	my_label = Label(image=image_list[i])
	my_label.grid(row=0,column=i, columnspan=3)
	# change index
	print(i)
	print(image_list[i])
	time.sleep(DELAY)
	# get rid on present image
	#my_label.grid_forget()
	


















root.mainloop()
