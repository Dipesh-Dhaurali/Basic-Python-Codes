import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Info", "This is an info message.")

def show_warning():
    messagebox.showwarning("Warning", "This is a warning message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

root = tk.Tk()
root.title("Message Box")
root.geometry("250x150")

tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)
tk.Button(root, text="Show Error", command=show_error).pack(pady=5)

root.mainloop()
