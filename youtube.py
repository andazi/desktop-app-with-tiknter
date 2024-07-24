import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        # get link
        ytLink = link.get()
        #
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        #video title
        videoTitle.configure(text=ytObject.title)
        # download it
        video.download()
        # success download
        finishDownload.configure(text="Downloaded succesfull",text_color='green')
        
    except Exception as e:
        finishDownload.configure(text="Download error", text_color='red') 
        print(e.message)

# progress
def on_progress(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percent_complete = (bytes_downloaded/total_bytes) * 100
    per_str = str(int(percent_complete))
    print(per_str)
    # percent
    progressPercent.configure(text=per_str+"%")
    progressPercent.update()
    # bar
    progressBar.set(float(percent_complete)/100)

# system settings
customtkinter.set_appearance_mode("System") # system appearance mode (light or dark or custom)
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# UI elements
# customtkinker.CTkLabel(frame, text,...)
# which frame you want to add the label
title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# download btn
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# finished downloading
videoTitle = customtkinter.CTkLabel(app, text="")
videoTitle.pack()
finishDownload = customtkinter.CTkLabel(app, text="")
finishDownload.pack()

# progress
progressPercent = customtkinter.CTkLabel(app, text="0%")
progressPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)






# run loop
app.mainloop()











