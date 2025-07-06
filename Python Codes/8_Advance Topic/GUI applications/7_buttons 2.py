import tkinter as tk
root= tk.Tk()


def hello():
    print("My name is Dipesh")

b1=tk.Button(root,text='click me',command=hello)
b1.pack()

root.mainloop()

