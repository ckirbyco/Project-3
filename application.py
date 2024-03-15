import requests
import matplotlib.pyplot as plt

#API Key


#Graph


#User Interface
def main():
  symbol = input("Enter the stock symbol: ").upper()
  print("Select the time series function:")
  print("1. Daily (TIME_SERIES_DAILY)")
  print("2. Weekly (TIME_SERIES_WEEKLY)")
  print("3. Monthly (TIME_SERIES_MONTHLY)")
  print("4. Intraday (TIME_SERIES_INTRADAY)")
  function_choice = input("Enter your choice (1/2/3/4): ")

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

if __name__ == "__main__":
def main()

  
