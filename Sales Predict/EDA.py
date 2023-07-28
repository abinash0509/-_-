import matplotlib.pyplot as plt

# Visualize sales over time
plt.plot(sales_data['date'], sales_data['sales'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend over Time')
plt.show()

# Analyze correlations between features
correlation_matrix = sales_data.corr()
