from tkinter import Tk, Text
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )


root = Tk()
root.resizable(False, True)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

download_icon = tk.PhotoImage(file='./assets/download.png')
download_button = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



root.mainloop()