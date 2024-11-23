import pandas as pd
import random
from faker import Faker
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


faker = Faker()
data = []

beverages = ['Cappuccino', 'Latte', 'Espresso', 'Mocha', 'Americano']
food_items = ['Croissant', 'Muffin', 'Bagel', 'Sandwich', 'Cake Slice']
payment_methods = ['Cash', 'Credit Card', 'Mobile Payment']
times_of_day = ['Morning', 'Afternoon', 'Evening']

for _ in range(1000):  
    transaction = {
        'Transaction ID': faker.uuid4(),
        'Customer ID': faker.uuid4(),
        'Customer Age': random.randint(16, 70),
        'Gender': random.choice(['Male', 'Female', 'Other']),
        'Beverage': random.choice(beverages),
        'Food Item': random.choice(food_items),
        'Quantity Sold': random.randint(1, 5),
        'Price per Item': round(random.uniform(2.5, 10), 2),
        'Order Time': random.choice(times_of_day),
        'Payment Method': random.choice(payment_methods),
        'Customer Rating': random.randint(1, 5)
    }
    transaction['Total Price'] = transaction['Quantity Sold'] * transaction['Price per Item']
    data.append(transaction)

df = pd.DataFrame(data)
df.to_excel("coffee_shop_sales.xlsx", index=False)
print("Sample dataset created: coffee_shop_sales.xlsx")
df = pd.read_excel("coffee_shop_sales.xlsx")
beverage_sales = df.groupby('Beverage')['Quantity Sold'].sum().sort_values(ascending=False)
beverage_sales.plot(kind='bar', title='Top-Selling Beverages')
plt.xlabel('Beverage')
plt.ylabel('Quantity Sold')
plt.show()
order_time = df['Order Time'].value_counts()
sns.barplot(x=order_time.index, y=order_time.values, palette='coolwarm')
plt.title('Peak Order Times')
plt.xlabel('Time of Day')
plt.ylabel('Number of Orders')
plt.show()
order_time = df['Order Time'].value_counts()
sns.barplot(x=order_time.index, y=order_time.values, palette='coolwarm')
plt.title('Peak Order Times')
plt.xlabel('Time of Day')
plt.ylabel('Number of Orders')
plt.show()
sns.histplot(df['Customer Age'], bins=10, kde=True, color='gold')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
avg_spending = df['Total Price'].mean()
print(f"Average Customer Spending: ${avg_spending:.2f}")
ratings = df['Customer Rating'].value_counts(normalize=True) * 100
sns.barplot(x=ratings.index, y=ratings.values, palette='viridis')
plt.title('Customer Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Percentage')
plt.show()

