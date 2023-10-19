#need to install matplotlib

import matplotlib.pyplot as plt

x = ['Q1','Q2','Q3','Q4']
y=[10000,12000,11000,8000]
plt.xLabel('Quarter')
plt.ylabel('Sales')
plt.title('Sales by Quarter')
plt.bar(x,y)
plt.show()