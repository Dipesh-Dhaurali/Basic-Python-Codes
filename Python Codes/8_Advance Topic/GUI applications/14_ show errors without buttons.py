import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

messagebox.showinfo("Info", "This is an info message.")
messagebox.showwarning("Warning", "This is a warning message.")
messagebox.showerror("Error", "This is an error message.")

root.destroy()  # Close the hidden main window
