# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def main():
    """
    Run all program functions
    """
    print(f"Welcome to Personal Expenses Tracker!")
    print(f"Please follow the instruction to enter your expense.")
    print(f"Exp: Name of the item, amount of the item, categroy of the item.")

    # Get expense from User
    get_expense_data()
    # Save expense to CSV file
    save_expense_to_file()
    # Summarise expense total
    expense_total()
    # show remainning budget    


def get_expense_data():
    """
    Get expense data from the user.
    Create three variable name, amount, categories to store data.
    Run a while loop for categories for user to select the valid data.
    The loop will repeatedly request data, until it is valid.
    """
    expense_name = str(input(f"Enter the name of the item:"))
    expense_amount = float(input(f"Enter the amount of the expense:"))
    
    expense_categories = [
        "Home",
        "Food",
        "Transportation",
        "Entertainment",
        "Others"
    ]
    while True:
        print(f"Please choose the relevent category:")
        # enumerate() converted into a list of tuples using the list().
        for ind, categeroy_name in enumerate(expense_categories):
            print(f"{ind}  {categeroy_name}")
        break


def save_expense_to_file():
    """
    
    """
    print(f"You have saved: ")


def expense_total():
    """
    
    """
    print(f"You have spend: ")


if __name__ == "__main__":
    main()
