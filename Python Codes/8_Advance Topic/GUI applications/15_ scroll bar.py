import tkinter as tk

root = tk.Tk()

text = tk.Text(root, wrap='none')
scrollbar = tk.Scrollbar(root, orient='vertical', command=text.yview)
text.config(yscrollcommand=scrollbar.set)

text.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

root.mainloop()
