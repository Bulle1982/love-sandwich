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



# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
