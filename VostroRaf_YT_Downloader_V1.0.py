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