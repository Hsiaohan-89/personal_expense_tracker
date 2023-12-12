# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from expense import Expense


def main():
    """
    Run all program functions
    """
    print(f"Welcome to Personal Expenses Tracker!")
    print(f"Please follow the instruction to enter your expense.")
    print(f"Exp: Name of item, amount of item, categroy of item.\n")

    # Get expense from User
    expense = get_expense_data()

    # Save expense to CSV file
    save_expense_to_file(expense)
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
    expense_amount = float(input("Enter the amount of the expense:"))

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
        # expept valueError for invlid input
        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_ind = int(
                input(f"Enter a category number {value_range}:")) - 1

            if 0 <= selected_ind < len(expense_categories):
                selected_category = expense_categories[selected_ind]
                print(f"You selected: {selected_category}")
                selected_category = expense_categories[selected_ind]
                new_expense = Expense(
                    name=expense_name, amount=expense_amount, category=selected_category
                )
                return new_expense
            else:
                print("invalid selection. Please enter a valid number.")
        except ValueError:
            print("invalid input. Please try again!")


def save_expense_to_file(expense):
    """

    """
    print(f"You have saved: {expense} ")


def expense_total():
    """

    """
    print(f"You have spend: ")


if __name__ == "__main__":
    main()
