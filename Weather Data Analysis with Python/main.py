import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
data = {
    "date": dates,
    "temperature": np.random.normal(30, 5, 100),
    "humidity": np.random.uniform(50, 85, 100),
    "precipitation": np.random.choice([0, 1, 2, 3, 4, 5], 100, p=[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]),
    "wind_speed": np.random.normal(10, 3, 100)
}

df = pd.DataFrame(data)
df["month"] = df["date"].dt.month

# Analysis
avg_temp = df["temperature"].mean()
max_temp_day = df.loc[df["temperature"].idxmax(), "date"]
avg_humidity = df["humidity"].mean()
total_precipitation = df["precipitation"].sum()

print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Day with Highest Temperature: {max_temp_day}")
print(f"Average Humidity: {avg_humidity:.2f}%")
print(f"Total Precipitation: {total_precipitation}mm")


plt.figure(figsize=(12, 6))
sns.lineplot(x="date", y="temperature", data=df, color="blue")
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x="month", y="temperature", data=df, estimator=np.mean, palette="coolwarm")
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 5))
sns.scatterplot(x="temperature", y="humidity", data=df, color="purple")
plt.title("Temperature vs. Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 5))
sns.heatmap(df[["temperature", "humidity", "precipitation", "wind_speed"]].corr(), annot=True, cmap="YlGnBu")
plt.title("Correlation Heatmap of Weather Variables")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="month", y="temperature", data=df, palette="coolwarm")
plt.title("Monthly Temperature Distribution")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df["precipitation"], bins=6, kde=True, color="darkblue")
plt.title("Precipitation Frequency Distribution")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Frequency")
plt.show()