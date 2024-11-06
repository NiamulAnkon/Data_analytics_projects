import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Date": pd.date_range(start="2020-01-01", periods=30, freq="Q"),
    "Revenue": np.random.randint(100000, 200000, size=30),
    "COGS": np.random.randint(50000, 100000, size=30),
    "Operating Expenses": np.random.randint(20000, 40000, size=30),
    "Net Income": np.random.randint(10000, 50000, size=30),
    "EPS": np.round(np.random.uniform(1.0, 5.0, size=30), 2)
}

df = pd.DataFrame(data)
df["Gross Profit"] = df["Revenue"] - df["COGS"]
df["Gross Profit Margin"] = (df["Gross Profit"] / df["Revenue"]) * 100

df.to_excel("/mnt/data/apple_income_statement_sample.xlsx", index=False)

plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Revenue"], label="Revenue", color="blue")
plt.plot(df["Date"], df["Net Income"], label="Net Income", color="green")
plt.xlabel("Date")
plt.ylabel("Amount")
plt.title("Revenue and Net Income Trend")
plt.legend()
plt.show()

average_gpm = df["Gross Profit Margin"].mean()
print(f"Gross Profit Margin (Average): {average_gpm:.2f}%")

latest_expenses = df.iloc[-1]["Operating Expenses"]
labels = ["Operating Expenses"]
sizes = [latest_expenses]
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Operating Expenses Breakdown - Last Quarter")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["EPS"], marker='o', color="purple")
plt.xlabel("Date")
plt.ylabel("EPS")
plt.title("Earnings Per Share (EPS) Over Time")
plt.show()

profitability_ratios = {
    "Net Profit Margin (%)": (df["Net Income"] / df["Revenue"]) * 100,
    "Return on Equity (ROE)": np.random.uniform(10, 20, size=30)
}
ratios_df = pd.DataFrame(profitability_ratios)
print("Profitability Ratios Overview:")
print(ratios_df.mean().round(2))
