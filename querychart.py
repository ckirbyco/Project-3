import requests
import pygal
from datetime import datetime

def fetch_stock_data(symbol, function, start_date, end_date):
    api_key = "WOGJ9FO9C2UDNNW6"  
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}&outputsize=full"
    response = requests.get(url)
    data = response.json()

    # Extract relevant data
    time_series_key = "Time Series (Daily)"
    dates = []
    values = []

    for date, info in data[time_series_key].items():
        current_date = datetime.strptime(date, "%Y-%m-%d")
        if start_date <= current_date <= end_date:
            dates.append(current_date)
            values.append(float(info["4. close"]))  # Closing price

    return dates, values

def plot_stock_data(dates, values, chart_type):
    chart = pygal.Line() if chart_type == "line" else pygal.Bar()
    chart.title = 'Historical Stock Data'
    for date, value in zip(dates, values):
        chart.add(str(date.date()), value)
    chart.x_labels = map(str, dates)
    chart.render_in_browser()

def main():
    symbol = input("Enter the stock symbol: ")
    function = input("Enter the time series function (e.g., TIME_SERIES_DAILY): ")
    chart_type = input("Enter the chart type (line/bar): ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Convert start_date and end_date strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Fetch stock data
    dates, values = fetch_stock_data(symbol, function, start_date, end_date)

    # Plot stock data
    plot_stock_data(dates, values, chart_type)

if __name__ == "__main__":
    main()