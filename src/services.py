from typing import Dict
import requests
from bs4 import BeautifulSoup
import datetime

def fetch_polygon_data(stock_symbol: str):
    # Change to the day before today, because the today date was returning me a error
    date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    api_key = "bs1n5Vdqoi_NOvmCZ_85rrcvtFnYN3vm"
    url = f"https://api.polygon.io/v1/open-close/{stock_symbol}/{date}?adjusted=True&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}

async def scrape_marketwatch_data(stock_symbol: str):
    mock_performance_data = {
    "1 Day": 1.23,
    "5 Day": 4.56,
    "1 Month": 7.89,
    "3 Month": 12.34,
    "YTD": 15.67,
    "1 Year": 18.90,
    "3 Year": 23.45,
    "5 Year": 26.78,
    "10 Year": 29.01
    }
    return mock_performance_data