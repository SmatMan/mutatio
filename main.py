from tkinter import Tk, Label, Button, Entry, IntVar, Radiobutton, filedialog
from tkinter.messagebox import showinfo
import youtube_dl
import os
from os.path import expanduser
import time
import platform
import subprocess

dirPath = expanduser("~")

class muatioGUI:

    def __init__(self, master):
        self.downloadPath = f'{dirPath}/Downloads'
        self.master = master
        master.title("Mutatio")
        self.url_entry = Entry()
        self.url_entry.pack(fill="none", expand=True)

        self.mp3_button = Button(master, text="Download as MP3", command=self.downloadMP3)
        self.mp3_button.pack(fill="none", expand=False)

        self.mp4_button = Button(master, text="Download as MP4", command=self.downloadMP4)
        self.mp4_button.pack(fill="none", expand=False)

        self.file_button = Button(master, text="Select a Folder", command=self.openFileSelector)
        self.file_button.pack(fill="none", expand=False)
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(fill="none", expand=True)

    def errorPopup(self, text: str):
        showinfo("Error", text)

    def infoPopup(self, text: str):
        showinfo("Info", text)

    def openDownloadLocation(self):
        if platform.system() == "Windows":
            os.startfile(self.downloadPath)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def downloadMP3(self):
        
        ydl_opts_mp3 = {

            'format': 'bestaudio/best',
            
            'outtmpl': f"{self.downloadPath}/%(title)s.%(ext)s",

            'updatetime': False,

            'postprocessors': [{

                'key': 'FFmpegExtractAudio',

                'preferredcodec': 'mp3',

                'preferredquality': '192',

            }],
        }

        print(self.downloadPath)
        try:
            with youtube_dl.YoutubeDL(ydl_opts_mp3) as ydl:
                ydl.download([f'{str(self.url_entry.get())}'])
                info = ydl.extract_info(str(self.url_entry.get()), download=False)
                video_title = info.get('title', None)
            self.openDownloadLocation()
            
            #self.infoPopup(f"Finished downloading {video_title}")
        except Exception as e:
            self.errorPopup(str(e))

    def downloadMP4(self):
        try:
            with youtube_dl.YoutubeDL({'format':'136+bestaudio', 'outtmpl':f"{self.downloadPath}/%(title)s.%(ext)s", 'updatetime': False}) as ydl:
                ydl.download([f'{str(self.url_entry.get())}'])
            self.openDownloadLocation()
        except Exception as e:
            self.errorPopup(str(e))

    def openFileSelector(self):
        self.downloadPath = filedialog.askdirectory()
        print(self.downloadPath)

root = Tk()
root.geometry('300x300')
gui = muatioGUI(root)
root.mainloop()