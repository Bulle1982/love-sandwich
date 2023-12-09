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
    while True:
        # Message to the user in the terminal
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        # Data input from the user stored in the variable data_str.
        data_str = input("Enter your data here: \n")
        # split the data_str and store it in a variable called sales_data.
        sales_data = data_str.split(",")
        #Call the function validate_data and pass sales_data.

        if validate_data(sales_data):
            print("Data is valid!")
            break
    return sales_data

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
                return False
    return True

# Refactored sales and surplus functions
'''
def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated succcessfully!\n")


def update_surplus_worksheet(data):
    """
    Update surplus worksheet, add new row with the list data provided.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated succcessfully!\n")
'''

def update_worksheet(data, worksheet):
    """
    Recieves a list of integers to be inserted into a worksheet.
    Update the relevant worksheet with the data provided.
    """
    print("Updating surplus worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated succcessfully!\n")

def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure subtracted from the stock:
    - Positive surplus indicates waste
    - Negative surplus indicates extra made when stock was sold out. 
    """
    print("Calculating surplus data..\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data  
    
def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, 
    collecting the last 5 entries for each sandwich and returns the data
    as a list. 
    """
    sales = SHEET.worksheet("sales")

    columns = []

    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])

    return columns    

def calculate_stock_stock(data):
    """
    Calculate the average stock for each item type, adding 10%
    """

    print("Calculating stock data...\n")
    new_stock_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data    

def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, "surplus")
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_stock_stock(sales_columns)
    update_worksheet(stock_data, "stock")
    return stock_data

print("Welcome to Love Sandwich Data Automation")
stock_data = main()    

# Write you code below this comment
def get_stock_values(data):
    '''
   - headings = SHEET.worksheet("stock").row_values(1): This line retrieves the values in the first row of the "stock" worksheet using SHEET.worksheet("stock").row_values(1). It assumes that the first row contains the headings for your data.

- stock_values = {head: value for head, value in zip(headings, data)}: This line uses a dictionary comprehension to create a dictionary (stock_values). It pairs each heading from the headings list with the corresponding value from the data list, creating key-value pairs in the dictionary.

- return stock_values: This line returns the resulting dictionary, where the keys are the headings and the values are the corresponding data values.

- In summary, the function takes a list of data (data) and assumes that the first row of the "stock" worksheet contains the headings. It then creates a dictionary (stock_values) where each heading is paired with its corresponding data value from the data list. The resulting dictionary represents the stock values with their respective headings.
'''
    headings = SHEET.worksheet("stock").row_values(1)
    stock_values = {head: value for head, value in zip(headings, data)}
    return stock_values
    

    
stock_values = get_stock_values(stock_data)
print("Stock Values:")
print(stock_values)