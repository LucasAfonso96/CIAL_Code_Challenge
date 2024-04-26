import requests
from bs4 import BeautifulSoup
import datetime
import os

def fetch_polygon_data(stock_symbol: str):
    date = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    api_key = os.environ.get("POLYGON_API_KEY")
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
    url = f"https://cloud.iexapis.com/stable/stock/{stock_symbol}/quote"
    
    try:
        response = requests.get(url)
        print('r', response)
        if response.status_code == 200:
            data = response.json()
            return {
                "Symbol": data["symbol"],
                "Latest Price": data["latestPrice"]
            }
    
    except Exception as e:
        # Log or handle the exception accordingly
        pass
    
    # If fetching data fails or data is not found, return None
    return None
    url = f"https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock_symbol,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "Time Series (Daily)" in data:
                latest_data = data["Time Series (Daily)"]
                latest_date = max(latest_data.keys())
                latest_close = float(latest_data[latest_date]["4. close"])
                return {
                    "Symbol": stock_symbol,
                    "Latest Close": latest_close
                }
    
    except Exception as e:
        # Log or handle the exception accordingly
        pass
    
    # If fetching data fails or data is not found, return None
    return None
    url = f'https://finance.yahoo.com/quote/{stock_symbol}'
    
    try:
        response = requests.get(url)
        print('r', response)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            verview_elements = soup.find("div", data_testid_="cards-4 contentContainer svelte-12wncuy mt")
            print('fora', verview_elements)
            if verview_elements:
                performance_section = verview_elements.find_parent("section")
                if performance_section:
                    performance_data = {}
                    
                    # Find all performance metrics
                    metrics = performance_section.find_all("h3", class_="title font-condensed svelte-1v51y3z clip")
                    perfInfo = performance_section.find_all("div", class_="perfInfo svelte-12wncuy")
                    
                    for metric, info in zip(metrics, perfInfo):
                        metric_title = metric.text.strip()
                        symbol = info.find("div", class_="symbol svelte-12wncuy").text.strip()
                        perf = info.find("div", class_="perf positive svelte-12wncuy") or info.find("div", class_="perf negative svelte-12wncuy")
                        if perf:
                            percentage = float(perf.text.strip().replace("%", ""))
                            performance_data[metric_title] = {
                                "Symbol": symbol,
                                "Percentage": percentage
                            }
                    
                    return performance_data
        
    except Exception as e:
        # Log or handle the exception accordingly
        pass
    
    # If scraping fails or data is not found, return an empty dictionary
    return {}