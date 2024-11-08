import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('global_temperature_anomaly.csv')

# Basic EDA
print(df.head())
print(df.describe())

# Visualize global temperature trend
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Global Temperature Anomaly'])
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.title('Global Temperature Anomaly Over Time')
plt.grid(True)
plt.show()

# Calculate the rate of temperature change
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Year'], df['Global Temperature Anomaly'])
print('Rate of temperature change:', slope, '°C/year')