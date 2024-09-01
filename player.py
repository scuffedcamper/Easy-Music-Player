import os

from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from ttkthemes import ThemedTk

ver = "1.0"

def getFolder():
    filepath = filedialog.askdirectory()
    return get_mp3_file_paths(filepath)

def get_mp3_file_paths(directory):
    mp3_file_paths = []
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if full_path.endswith('.mp3'):
            mp3_file_paths.append(full_path)
    print(mp3_file_paths)
    return mp3_file_paths

playWin = ThemedTk(theme = "equilux")
playWin.configure(bg="grey28")

musicList = ttk.Combobox()
#musicList['values'] = 

#label
title = ttk.Label(text = "Music Player - Ver: " + ver, font = ('Segoe UI', 18))
title.grid(row=0, column = 0, pady = 30)

#get music directory button
usrFolder = ttk.Button(text="Choose Music Directory", command=getFolder)
usrFolder.grid(row = 1, column = 0, sticky = "W")










playWin.mainloop()

