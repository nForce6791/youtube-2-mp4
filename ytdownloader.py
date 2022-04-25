import os
import tkinter
from tkinter import *

#create a tkinter window
window = tkinter.Tk()
window.title("YouTube Downloader")
window.geometry("600x500")

#create a simple gui 
label = tkinter.Label(window, text = "YouTube Downloader", font = "Helvetica 16 bold")
label.grid(column = 0, row = 0)


#allow user to input a youtube link
label = tkinter.Label(window, text = "YouTube Link:")
label.grid(column = 0, row = 1)

#define entry
entry = tkinter.Entry(window, width = 50)
entry.grid(column = 1, row = 1)

#download the youtube video inputted by user
def download():
    os.chdir("cd C:\\Users\\%username%\\Downloads")
    os.system("youtube-dl -o %(title)s.%(ext)s " + entry.get())
    

#create a download button
download_button = tkinter.Button(window, text = "Download", command = download)
download_button.grid(column = 1, row = 3)



window.mainloop()
