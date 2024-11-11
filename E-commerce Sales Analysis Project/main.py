import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
categories = ['Electronics', 'Clothing', 'Home Decor', 'Books']
regions = ['North', 'South', 'East', 'West']
data = {
    "OrderID": np.arange(1, 101),
    "Date": dates,
    "Product": [f'Product_{i}' for i in range(1, 101)],
    "Category": np.random.choice(categories, 100),
    "Region": np.random.choice(regions, 100),
    "Quantity": np.random.randint(1, 10, 100),
    "UnitPrice": np.round(np.random.uniform(10, 200, 100), 2)
}

df = pd.DataFrame(data)
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

df["Month"] = df["Date"].dt.month

total_sales = df["TotalPrice"].sum()
avg_order_value = df["TotalPrice"].mean()
total_orders = df["OrderID"].nunique()
top_category = df.groupby("Category")["TotalPrice"].sum().idxmax()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Order Value: ${avg_order_value:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Top Sales Category: {top_category}")


plt.figure(figsize=(10, 6))
monthly_sales = df.groupby("Month")["TotalPrice"].sum()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='blue')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
top_products = df.groupby("Product")["TotalPrice"].sum().nlargest(5)
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 5 Products by Sales")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
category_aov = df.groupby("Category")["TotalPrice"].mean()
sns.barplot(x=category_aov.index, y=category_aov.values, palette="muted")
plt.title("Average Order Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Order Value ($)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
region_sales = df.groupby("Region")["TotalPrice"].sum()
sns.barplot(x=region_sales.index, y=region_sales.values, palette="pastel")
plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()
