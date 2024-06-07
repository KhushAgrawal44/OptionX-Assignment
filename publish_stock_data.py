import redis
import time
import json
from datetime import datetime
import random
import pytz

# Connect to the local Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Stock symbols
stocks = ["HDFC", "TATAMOTORS", "HAL", "RELIANCE", "LIC"]

# Function to generate stock data
def generate_stock_data(symbol):
   
    india_timezone = pytz.timezone('Asia/Kolkata')
    return {
        "timestamp":  datetime.now(india_timezone).isoformat(),
        "symbol": symbol,
        "price": round(random.uniform(100, 200), 2),
        "quantity": random.randint(1, 100)
    }

# Publish data every second
try:
    while True:
        for stock in stocks:
            data = generate_stock_data(stock)
            r.publish('stock_channel', json.dumps(data))
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped publishing data.")
