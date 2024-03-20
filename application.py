import requests
import matplotlib.pyplot as plt

#API Key


#Graph


#User Interface
def main():
  symbol = input("Enter the stock symbol you are looking for: ").upper()
  
  print("Select the time series function for the chart you want to generate:")
  print("1. Daily (TIME_SERIES_DAILY)")
  print("2. Weekly (TIME_SERIES_WEEKLY)")
  print("3. Monthly (TIME_SERIES_MONTHLY)")
  print("4. Intraday (TIME_SERIES_INTRADAY)")
  function_choice = input("Enter time series option (1, 2, 3, 4): ")

  if function_choice == '1':
    function = 'TIME_SERIES_DAILY'
  elif function_choice == '2':
    function = 'TIME_SERIES_WEEKLY'
  elif function_choice == '3':
    function = 'TIME_SERIES_MONTHLY'
  elif function_choice == '4':
    function = 'TIME_SERIES_INTRADAY'
  else:
      print("Invalid choice. Please select 1, 2, 3, or 4.")
      return

  start_date = input("Enter the beginning date in YYYY-MM-DD format: ")
  end_date = input("Enter the end date in YYYY-MM-DD format: ")
  chart_type = input("Enter the chart type (line/bar/scatter): ").lower()

if start_date > end_date:
  print("Error: End date cannot be before the begin date.")
  return

  #Hold API key for Alpha Vantage 
  api_key = "AU63WJRRMDHJZX92"


if __name__ == "__main__":
def main()

  
