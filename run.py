import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwich")

"""
sales = SHEET.worksheet("sales")
sales_data = sales.get_all_values()
print("Below is the sales data:")
print(sales_data)

stock = SHEET.worksheet("stock")
stock_data = sales.get_all_values()
print("Below is the stock data:")
print(stock_data)


surplus = SHEET.worksheet("surplus")
surplus_data = sales.get_all_values()
print("Below is the surplus data:")
print(surplus_data)

"""

def get_sales_data():
    """
    Get sales figures input from the user
    """

    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    # print(f"The data provided is: {data_str}")
    sales_data = data_str.split(",")
    validate_data(sales_data)
    #print(sales_data)

def validate_data(values):
    """
    Inside the try, converts all the string values into integers.
    Raises ValuError if strings cannot be converted into int,
    or if there are no exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")

get_sales_data()    
