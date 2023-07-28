# Handle missing values, duplicates, and outliers
sales_data.dropna(inplace=True)
sales_data.drop_duplicates(inplace=True)

# Convert categorical variables into numerical representations
sales_data = pd.get_dummies(sales_data, columns=['product_category'], drop_first=True)
