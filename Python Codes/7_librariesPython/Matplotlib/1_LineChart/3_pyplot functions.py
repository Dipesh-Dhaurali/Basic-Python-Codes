"""
cont...(1:11:50)
"""
import matplotlib.pyplot as plt

months=[1,2,3,4]
sales=[1000,1500,1200,1800]

plt.plot(months,sales,color='blue',linestyle='--',marker='o',label='2025 sales data')

plt.xlabel('months')
plt.ylabel('sales')
plt.title("Monthly sales report")
plt.grid(linestyle=':')
plt.legend()

plt.show()