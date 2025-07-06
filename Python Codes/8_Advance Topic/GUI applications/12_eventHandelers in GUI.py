import tkinter as tk
root = tk.Tk()
root.title("Event Handler Example")


def on_button_click():
    label.config(text="Button was clicked!")


label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
