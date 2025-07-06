import tkinter as tk
from tkinter import StringVar

root= tk.Tk()
root.geometry("400x400")
user=StringVar()
psw=StringVar()
DOB=StringVar()

def show():
    print(user.get(),psw.get(),DOB.get())

def cls():
    user.set("")
    psw.set("")
    DOB.set("")

tk.Label(root,text="Username")  .     grid(row=0,column=0)
tk.Label(root,text="Password")  .     grid(row=1,column=0)
tk.Label(root,text="Date of birth") . grid(row=2,column=0)


tk.Entry(root,textvariable=user).grid(row=0,column=1)
tk.Entry(root,textvariable=psw).grid(row=1,column=1)
tk.Entry(root,textvariable=DOB).grid(row=2,column=1)


#rest and submit buttons
tk.Button(root,text="Submit",command=show).grid(row=6,column=0)
tk.Button(root,text="Rest",command=cls).grid(row=6,column=1)
root.mainloop()
