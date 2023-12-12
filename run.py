# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def main():
    """
    Run all program functions
    """
    print(f"Welcome to Personal Expenses Tracker!")
    print(f"Please follow the instruction to enter your expense.")
    print(f"Exp: Name of item, amount of item, categroy of item.\n")

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
    expense_name = input(f"Enter the name of the item:")
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
            print(f"{ind + 1}  {categeroy_name}")

        # Range of the selection for user to select
        # try:
        #     selected_ind = int(input(f"Enter a category number:"))
        #     if 1 <= selected_ind <= len(expense_categories):
        #         expense_categories = expense_categories[selected_ind - 1]
        #         print(f"You selected: {expense_categories}")
        #         raise NameError(
        #             f"Please enter a valid number, you provided {selected_ind}"
        #         )
        # except NameError as e:
        #     print(f"Invalid input: {e} Please try again.")
        value_range = f"[1 - {len(expense_categories)}]"
        
        selected_ind = int(input(f"Enter a category number {value_range}:")) -1

        # check for the value range
        if selected_ind in range(len(expense_categories)):
            break
        else:
            print("Invalid category. Please try again!")


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
