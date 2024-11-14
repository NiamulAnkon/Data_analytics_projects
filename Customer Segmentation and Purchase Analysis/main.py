#import area
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#data area
np.random.seed(42)
data = pd.DataFrame({
    'customer_id': range(1, 101),
    'age': np.random.randint(18, 70, size=100),
    'annual_income': np.random.randint(20000, 120000, size=100),
    'average_order': np.random.randint(50, 500, size=100),
    'purchase_frequency': np.random.randint(1, 20, size=100),
    'spending_score': np.random.randint(1, 100, size=100),
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=100)
})
data.head()

print(data.info())
print(data.describe())

plt.figure(figsize=(8, 6))
sns.histplot(data['annual_income'], bins=20, kde=True)
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='region', y='spending_score')
plt.title('Spending Score by Region')
plt.show()
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='average_order', y='spending_score', hue='region')
plt.title('Average Order Size vs Spending Score')
plt.show()
def categorize_spending(row):
    if row['spending_score'] >= 70:
        return 'High'
    elif row['spending_score'] >= 40:
        return 'Medium'
    else:
        return 'Low'

data['spending_category'] = data.apply(categorize_spending, axis=1)
data['spending_category'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Customer Segmentation by Spending Score')
plt.show()
plt.figure(figsize=(8, 6))
sns.histplot(data['purchase_frequency'], bins=20, kde=True)
plt.title('Purchase Frequency Distribution')
plt.xlabel('Number of Purchases')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(10, 8))
sns.scatterplot(data=data, x='annual_income', y='purchase_frequency', hue='spending_category')
plt.title('Annual Income vs. Purchase Frequency by Spending Category')
plt.show()
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, x='spending_category', y='average_order')
plt.title('Average Order Size by Spending Category')
plt.show()
high_spenders = data[data['spending_category'] == 'High']
print("Average Income of High Spenders:", high_spenders['annual_income'].mean())
print("Average Purchase Frequency of High Spenders:", high_spenders['purchase_frequency'].mean())

print("Total number of customers:", len(data))
print("Number of high spenders:", len(high_spenders))
print("Average annual income across all customers:", data['annual_income'].mean())

