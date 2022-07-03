from tkinter import *
from turtle import window_height
import youtube_dl

# initialising the app root base 
app_base = Tk()

# setting the basic config 
app_base.title('Youtube Video Downloader - VostroRaf007')
app_base.iconbitmap(r"icon.ico")
app_base.resizable(False, False)

# giving the measurements 
app_height = 500
app_width = 500

# providing the background color 
app_base.config(bg='blue')

# setting the window(screen) width 
window_width = app_base.winfo_screenwidth()
window_height = app_base.winfo_screenheight()

x_val = int(window_width - app_width) / 2
y_val = int(window_height - app_height) / 2

# passing the set values as the app geometry 
app_base.geometry(f"{app_width}x{app_height}+{x_val}+{y_val}")

# initialising an empty dictionary 
youtube_dl_dict = {}

# defining the download function 
def download():
    video_link = Vostro.get()
    link_strip_txt = video_link.strip()
    with youtube_dl.YoutubeDL(youtube_dl_dict) as downloads:
        downloads.download([link_strip_txt])

# defining a rerun callback function incase any error or event occurs
def rerun(instance):
    if Vostro.get() == "Paste the video link here.":
        Vostro.delete(0, "end")

# Assigning the head label
head_label = Label(app_base, text = 'High Quality Youtube video downloader from VostroRaf', fg = "white", bg = "blue")

# defining the entry point for the app
Vostro = Entry(app_base)
Vostro.config(font = ('arial', 15), width = 30)
Vostro.insert(END, "Paste the video link here.")
Vostro.bind("<Button-1>", rerun)
Vostro.place(x = 25, y = 120)
button = Button(app_base, text = "Get it!", bg = "darkblue", fg = "white", font = ('arial', 18))
app_base.mainloop()