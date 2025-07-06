import tkinter as tk
from tkinter import PhotoImage

root= tk.Tk()

#lable is for photo
img=PhotoImage(file="8.png")
label=tk.Label(root,image=img)
label.pack()

root.mainloop()