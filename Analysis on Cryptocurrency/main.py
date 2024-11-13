import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

cryptos = ["Bitcoin", "Ethereum", "Ripple", "Litecoin", "Cardano"]
num_days = 100  
start_date = datetime.now() - timedelta(days=num_days)

def generate_crypto_data():
    data = []
    for crypto in cryptos:
        date = start_date
        for _ in range(num_days):
            open_price = round(random.uniform(50, 1000), 2)
            close_price = round(open_price + random.uniform(-10, 10), 2)
            high_price = max(open_price, close_price) + random.uniform(0, 10)
            low_price = min(open_price, close_price) - random.uniform(0, 10)
            volume = random.randint(1000, 100000)
            market_cap = round(volume * close_price, 2)
            
            data.append({
                "Date": date,
                "Cryptocurrency": crypto,
                "Opening Price": open_price,
                "Closing Price": close_price,
                "High Price": high_price,
                "Low Price": low_price,
                "Volume": volume,
                "Market Cap": market_cap
            })
            date += timedelta(days=1)
    return data

crypto_data = generate_crypto_data()
df = pd.DataFrame(crypto_data)

file_path = "/mnt/data/crypto_data.xlsx"
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")
