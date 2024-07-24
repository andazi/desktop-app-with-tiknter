from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()

root.title("icons")


icon_path = "angelo_logo.png"

# check if icon exist
if os.path.exists(icon_path):
	try:
		# load img
		icon_img = Image.open(icon_path)
		icon_photo = ImageTk.PhotoImage(icon_img)
		
		# set the window
		root.iconphoto(False, icon_photo)
	except Exception as e:
		print(f"Error setting icon:{e}")
else:
	print("File not found at path", icon_path)


# center the app
root.eval("tk::PlaceWindow . center")
# window size
x = root.winfo_screenwidth() // 2 - 250 # center of the screen
y = int(root.winfo_screenheight() * 0.1) # 10% away from the top
# this create a fixed window size
root.geometry("500x600+" + str(x) + "+" + str(y))































root.mainloop()
