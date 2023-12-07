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
    # Message to the user in the terminal
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

     # Data input from the user stored in the variable data_str.
    data_str = input("Enter your data here: ")
    # split the data_str and store it in a variable called sales_data.
    sales_data = data_str.split(",")
    #Call the function validate_data and pass sales_data.
    validate_data(sales_data)
   

def validate_data(values):
    """
    Inside the try, all the string values are converted into integers.
    Raises ValuError if strings cannot be converted into int,
    or if there are no exactly 6 values
    """
    print(values)
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")

get_sales_data()    
