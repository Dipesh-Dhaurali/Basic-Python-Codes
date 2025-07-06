"""
https://youtu.be/kM_eVEEWfnE (1:30:00)
"""
import matplotlib.pyplot as plt

product=['A','B','C','D']
sales=[1000,1500,1200,1800]

plt.bar(product,sales,color='blue',label='2025 sales data')

plt.xlabel('months')
plt.ylabel('sales')
plt.title("Monthly sales report")
plt.legend()

plt.show()