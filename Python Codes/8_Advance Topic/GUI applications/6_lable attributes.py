"""
#6
"""
import tkinter as tk
from tkinter.constants import SUNKEN, GROOVE

root= tk.Tk()
root.title("Static Application")
root.geometry("1920x1080")

label=tk.Label(root,text="My name is Dipesh Dhaurali",
               bg="red",fg='white',
               font="comicsansms 18 bold",
               padx=30,pady=20,
               border=14,relief=GROOVE)

label.pack()
root.mainloop()