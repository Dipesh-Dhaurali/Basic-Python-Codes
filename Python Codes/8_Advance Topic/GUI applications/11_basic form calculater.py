import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.title("Addition Form")

# Variables to store input and result
a = StringVar()
b = StringVar()
result = StringVar()

# Function to perform addition
def add():
    try:
        num1 = int(a.get())
        num2 = int(b.get())
        result.set(str(num1 + num2))
    except ValueError:
        result.set("Invalid input")

# Function to clear the form
def clear():
    a.set("")
    b.set("")
    result.set("")

# Labels
tk.Label(root, text="Enter A:").grid(row=0, column=0)
tk.Label(root, text="Enter B:").grid(row=1, column=0)
tk.Label(root, text="Result:").grid(row=2, column=0)

# Entry fields
tk.Entry(root, textvariable=a).grid(row=0, column=1)
tk.Entry(root, textvariable=b).grid(row=1, column=1)
tk.Entry(root, textvariable=result, state="readonly").grid(row=2, column=1)

# Buttons
tk.Button(root, text="Add", command=add).grid(row=3, column=0)
tk.Button(root, text="Clear", command=clear).grid(row=3, column=1)

root.mainloop()
