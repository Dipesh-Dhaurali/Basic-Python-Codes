"""
cont... (1:32:00)
"""


import matplotlib.pyplot as plt

product=['A','B','C','D']
sales=[1000,1500,1200,1800]

plt.pie(sales,labels=product,autopct='%1.1f%%')

plt.xlabel('months')
plt.ylabel('sales')
plt.title("Monthly sales report")
plt.legend()

plt.show()