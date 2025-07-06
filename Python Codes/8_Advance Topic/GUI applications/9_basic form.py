#https://youtu.be/XExY7ZH31-E
#https://youtu.be/Rg96iAgQlfg?list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA\

import tkinter as tk
from tkinter import StringVar

root= tk.Tk()

#baisc
tk.Label(root,text="Username")  .     grid(row=0,column=0)
tk.Label(root,text="Password")  .     grid(row=1,column=0)
tk.Label(root,text="Date of birth") . grid(row=2,column=0)


tk.Entry(root).grid(row=0,column=1)
tk.Entry(root).grid(row=1,column=1)
tk.Entry(root).grid(row=2,column=1)

#for checkbox
#using booleanVar() for checkbox (Checkbox with grid layout)
apple=tk.BooleanVar()
mango=tk.BooleanVar()
banana=tk.BooleanVar()
papaya=tk.BooleanVar()

tk.Label(root,text="Food names to select:").grid(row=3,column=0)
tk.Checkbutton(root,text="Apple",variable=apple).grid(row=3,column=1)
tk.Checkbutton(root,text="Mango",variable=mango).grid(row=3,column=2)
tk.Checkbutton(root,text="Banana",variable=banana).grid(row=3,column=3)
tk.Checkbutton(root,text="Papaya",variable=papaya).grid(row=3,column=4)


#for radioButton()
#for radioButton(), we need to use IntVar() with common variable name
gender=tk.IntVar()
tk.Label(root,text="Gender:").grid(row=4,column=0)
tk.Radiobutton(root,text="Male",variable=gender,value=0).grid(row=4,column=1)
tk.Radiobutton(root,text="Female",variable=gender,value=1).grid(row=4,column=2)
tk.Radiobutton(root,text="Others",variable=gender,value=2).grid(row=4,column=3)

#for dropdown menu
#
tk.Label(root,text="Select Days: ").grid(row=5,column=0)
options=[
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
clicked=StringVar()
clicked.set(options[0])  #to select default value
tk.OptionMenu(root,clicked,*options).grid(row=5,column=1)



#rest and submit buttons
tk.Button(root,text="Submit").grid(row=6,column=0)
tk.Button(root,text="Rest").grid(row=6,column=1)



root.mainloop()

