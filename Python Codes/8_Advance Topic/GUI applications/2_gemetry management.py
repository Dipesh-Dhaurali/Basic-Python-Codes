"""
#4
1) geometry to give size of GUI
2) minsize to give minimum size of GUI
2) Maxsize to give Maximum size of GUI
"""
import tkinter as tk
root= tk.Tk()

####################################gemetry management ################
# "weight x height" (no space)
root.geometry("1920x1080")
#weight, height
root.minsize(400,400)
#weight, height
root.maxsize(1920,1080)

root.mainloop()
