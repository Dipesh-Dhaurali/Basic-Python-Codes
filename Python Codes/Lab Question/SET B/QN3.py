"""
Write a program that builds a basic calculator using
Tkinter with buttons for digits and operations
"""
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for showing input and result
entry = tk.Entry(root, width=35, borderwidth=10)
entry.grid(row=0, column=0, columnspan=5)

# List of buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create buttons and arrange them in a grid
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=10, height=4,
              command=lambda b=button: on_button_click(b)).grid(row=row, column=col)
    col=col+1
    if col > 3:
        col = 0
        row=row+1


# Function to handle button clicks
def on_button_click(button):
    if button == "=":
        result = eval(entry.get())       #entry.get() ==> "5+3"
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

root.mainloop()
