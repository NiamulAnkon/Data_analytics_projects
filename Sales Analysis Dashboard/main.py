import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta


sns.set(style="whitegrid")


np.random.seed(42)
n = 200  
data = {
    "Order ID": np.arange(1, n + 1),
    "Date": [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n)],
    "Product Category": np.random.choice(["Electronics", "Clothing", "Home Goods"], size=n),
    "Product Name": np.random.choice(["Product A", "Product B", "Product C", "Product D"], size=n),
    "Quantity Sold": np.random.randint(1, 10, size=n),
    "Unit Price": np.random.uniform(10, 500, size=n).round(2),
    "Customer ID": np.random.randint(1000, 1050, size=n),
    "Region": np.random.choice(["North", "South", "East", "West"], size=n)
}

df = pd.DataFrame(data)

df['Sales'] = df['Quantity Sold'] * df['Unit Price']

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

top_products = df.groupby('Product Name')['Quantity Sold'].sum().nlargest(5)

plt.figure(figsize=(8, 5))
top_products.plot(kind='bar', color='skyblue')
plt.title('Top 5 Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.show()

region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'salmon', 'gold'])
plt.title('Sales by Region')
plt.ylabel('')
plt.show()

customer_purchases = df['Customer ID'].value_counts()

plt.figure(figsize=(10, 6))
sns.histplot(customer_purchases, bins=10, kde=True, color="purple")
plt.title('Customer Purchase Frequency')
plt.xlabel('Number of Purchases')
plt.ylabel('Frequency')
plt.show()

category_sales = df.groupby('Product Category')['Sales'].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind='bar', color='coral')
plt.title('Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()

summary = df.describe()
print("\nSummary Statistics:")
print(summary)
