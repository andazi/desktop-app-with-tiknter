from tkinter import *
from PIL import ImageTk, Image 
import time
import os


root = Tk()

root.geometry("400x500")
root.eval("tk::PlaceWindow . center")

# frame in root
frame_img = Tk.frame(root, width=500, height=600, bg="red").pack(pady=10, padx=10)
frame_img.grid_propagate(False)


DELAY = 0.1

imgs = os.listdir("images")

# clear initial widget		
def clear_widget(frame):
	for widget in frame.winfo_children():
		print(frame)
		widget.destroy()

for pic in imgs:
	pic = f"images/{pic}"
	print(pic)
	img = ImageTk.PhotoImage(Image.open(pic))

	my_label = Label(image=img).pack()
	time.sleep(DELAY)
	clear_widget(root)
	


btn_quit = Button(root, text="Exit", command=root.quit).pack()



























root.mainloop()
