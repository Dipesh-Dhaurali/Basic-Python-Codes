"""
Create a line plot and scatter plot using Matplotlib,
customizing markers, colors, and labels.
"""
import matplotlib.pyplot as plt

months = [1,2,3,4,5]  # x-axis
avg_temp = [2, 3, 5, 7, 11]  # y-axis for line plot
tourists = [1, 4, 6, 8, 10]  # y-axis for scatter plot


# line plot
plt.plot(months, avg_temp, color='blue', linestyle='--', marker='o', label='Avg Temp (°C)')

# scatter plot
plt.scatter(months, tourists, color='red', marker='D', label='Tourists visit nepal')

plt.xlabel('Months')
plt.ylabel('Temperature / Tourists')
plt.title("Tourism vs Temperature (Jan–Apr)")
plt.grid(linestyle=':')
plt.legend()

plt.show()
