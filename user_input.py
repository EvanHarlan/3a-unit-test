from datetime import datetime
import re

class UserInput:

    """
    Function to get the stock symbol
    Returns a string: symbol
    """
    def get_symbol(self):
        while True:
            symbol = input("Enter the stock symbol you are looking for: ")
            if not self.isValidString(symbol):
                print("ERROR: please enter a stock symbol!\n")
            else:
                return symbol
    
    """
    Function to get the chart type
    Reuturns a string: chart type (1 or 2)
    """
    def get_chart_type(self):
        valid_selections = ["1", "2"]
        while True:
            self.printChartMenu()
            chart_type = input("Enter the chart type you want (1, 2): ")
            if not self.isValidString(chart_type) or chart_type not in valid_selections :
                print("ERROR: please enter a valid chart type!\n")
            else:
                return chart_type
            
    """
    Function to get the time series
    Reuturns a string: time series option (1, 2, 3, or 4)
    """
    def get_time_series(self):
        valid_selections = ["1", "2", "3", "4"]
        while True:
            self.printTimeSriesMenu()
            time_series_option = input("Enter time series option (1, 2, 3, 4): ")
            if not self.isValidString(time_series_option) or time_series_option not in valid_selections :
                print("ERROR: please enter a valid time series option!\n")
            else:
                return time_series_option


    """
    Function to print chart type menu
    Returns: none
    """
    def printChartMenu(self):
        print("\nChart Types\n-------------")
        print("1. Bar")
        print("2. Line\n")


    """
    Function to print time series type menu
    Returns: none
    """
    def printTimeSriesMenu(self):
        print("\nSelect the Time Series of the chart you want to Generate")
        print("--------------------------------------------------------")
        print("1. Intraday")
        print("2. Daily")
        print("3. Weekly")
        print("4. Monthly\n")

    """
    Function to validate sting input
    Parameters: the_string (the string to be validated)
    Returns: True if valid, False if not valid
    """
    def isValidString(self, the_string):
        if the_string == "":
            return False
        else:
            return True


    """
    Function to get date
    Returns: a string in date format
    """
    def get_date(self, period):
        prompt = f"Enter the {period} Date (YYYY-MM-DD): "
        date_regex = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
        
        while True:
            the_date = input(prompt)
            if re.match(date_regex, the_date):
                try:
                    #return the date as a date object
                    return datetime.strptime(the_date, "%Y-%m-%d")
                except ValueError as err:
                    print(f"ERROR: {str(err)}\n")

            else:
                print("ERROR: Enter the date in correct (YYYY-MM-DD) format! \n")


    """
    Function to compare start date to end date
    Parameters: start_date, end_date
    Returns: True if end_date > start_date, False if not valid
    """    
    def valid_date_range(self, start_date, end_date):
        if start_date >= end_date:
            print("ERROR: Start date cannot be later than end date. Enter the dates again.\n")
            return False
        else:
            return True
