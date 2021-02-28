from tkinter import Tk, Label, Button, Entry, IntVar, Radiobutton
from youtube_dl import YoutubeDL

class muatioGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mutatio")

        self.label = Label(master, text="Mutatio")
        self.label.pack()

        self.url_entry = Entry()
        self.url_entry.pack()

        format_selector = IntVar()
        self.mp3 = Radiobutton(root, text="MP3", value="mp3", variable=format_selector)
        self.mp4 = Radiobutton(root, text="MP4", value="mp4", variable=format_selector)
        self.mp3.pack()
        self.mp4.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print(self.url_entry.get())
root = Tk()
gui = muatioGUI(root)
root.mainloop()