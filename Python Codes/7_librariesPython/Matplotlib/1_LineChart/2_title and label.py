"""
title and labels
"""
import matplotlib.pyplot as plt
x=['mon','tues','wed','thurs','fri'] #x-axis
y=[10,15,7,20,12] #y-axis

plt.plot(x,y)

#title of the graph
plt.title("Bakery Sales this week")

#lables of the graph
plt.xlabel("Day of the week")
plt.ylabel("Sales per Day")

plt.show()
