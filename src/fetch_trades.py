# src/fetch_trades.py
import requests
import json

def fetch_trades(api_key: str, save_path="data/trades.json"):
    headers = {"Authorization": f"Bearer {api_key}"}
    url = "https://api.quiverquant.com/beta/historical/congresstrading"
    r = requests.get(url, headers=headers)
    data = r.json()
    with open(save_path, "w") as f:
        json.dump(data, f)
    return data
