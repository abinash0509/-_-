import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load unemployment rate data (assuming it's in a CSV file)
data = pd.read_csv('unemployment_data.csv')

# Display the first few rows of the data to understand its structure
print(data.head())

# Calculate average unemployment rate
average_unemployment = data['unemployment_rate'].mean()
print("Average Unemployment Rate:", average_unemployment)

# Calculate minimum and maximum unemployment rates
min_unemployment = data['unemployment_rate'].min()
max_unemployment = data['unemployment_rate'].max()
print("Minimum Unemployment Rate:", min_unemployment)
print("Maximum Unemployment Rate:", max_unemployment)

# Set the style for the plots
sns.set(style="whitegrid")

# Create a line plot to visualize unemployment rate over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='unemployment_rate')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.xticks(rotation=45)
plt.show()
