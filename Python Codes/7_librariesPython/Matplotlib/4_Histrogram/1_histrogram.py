"""
https://youtu.be/kM_eVEEWfnE (1:39:z00)
"""
import matplotlib.pyplot as plt

scores=[47, 12, 89, 65, 34, 77, 23, 90, 58, 6, 39, 71, 2, 84, 51]

plt.hist(scores,bins=5,color='blue',edgecolor='black',label='2025 sales data')

plt.xlabel('months')
plt.ylabel('sales')
plt.title("Monthly sales report")
plt.legend()

plt.show()