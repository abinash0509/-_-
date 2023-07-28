# Example: Adding lag features
sales_data['previous_day_sales'] = sales_data['sales'].shift(1)

# Example: Adding rolling averages
sales_data['rolling_avg_7days'] = sales_data['sales'].rolling(window=7).mean()
