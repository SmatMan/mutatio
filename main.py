from tkinter import Tk, Label, Button, Entry, IntVar, Radiobutton
from tkinter.messagebox import showinfo
import youtube_dl

ydl_opts_mp3 = {

    'format': 'bestaudio/best',
    
    'outtmpl': '%(title)s.%(ext)s',

    'postprocessors': [{

        'key': 'FFmpegExtractAudio',

        'preferredcodec': 'mp3',

        'preferredquality': '192',

    }],

}

class muatioGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mutatio")

        self.label = Label(master, text="Mutatio")
        self.label.pack()

        self.url_entry = Entry()
        self.url_entry.pack()

        self.mp3_button = Button(master, text="Download as MP3", command=self.downloadMP3)
        self.mp3_button.pack()

        self.mp4_button = Button(master, text="Download as MP4", command=self.downloadMP4)
        self.mp4_button.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def errorPopup(self, text: str):
        showinfo("Error", text)

    def downloadMP3(self):
        try:
            with youtube_dl.YoutubeDL(ydl_opts_mp3) as ydl:
                ydl.download([f'{str(self.url_entry.get())}'])
        except Exception as e:
            self.errorPopup(str(e))

    def downloadMP4(self):
        with youtube_dl.YoutubeDL({'format':'136+bestaudio', 'outtmpl':'%(title)s.%(ext)s'}) as ydl:
            ydl.download([f'{str(self.url_entry.get())}'])

    

root = Tk()
gui = muatioGUI(root)
root.mainloop()