# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from expense import Expense
import calendar
import datetime


def main():
    """
    Run all program functions
    """
    print(f"Welcome to Personal Expenses Tracker!")
    print(f"Please follow the instruction to enter your expense.")
    print(f"Exp: Name of item, costs of item, categroy of item.\n")
    # Declaring a file name
    expense_file_path = "expenses.csv"

    budget = 500

    # Get expense from User
    expense = get_expense_data()

    # Save expense to CSV file
    save_expense_to_file(expense, "expenses.csv")

    # Summarise expense total
    summarise_expense(expense_file_path, budget)

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
                    name=expense_name, amount=expense_amount,
                    category=selected_category
                )
                return new_expense
            else:
                print("invalid selection. Please enter a valid number.")
        except ValueError:
            print("invalid input. Please try again!")


def save_expense_to_file(expense, expense_file_path):
    """
    Store input expense data into expense csv file.
    """
    print(f"Saving expense: {expense} to {expense_file_path}\n ")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarise_expense(expense_file_path, budget):
    """
    Summarize the total expense by read each line category 
    create if else statement for stating overbudget or how much you can spent
    on each day.
    """

    expenses = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_categories = stripped_line.split(
                ",")

            line_expense = Expense(
                name=expense_name, amount=float(expense_amount),
                category=expense_categories)
            expenses.append(line_expense)

    # Create a dict to get each items
    total_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in total_by_category:
            total_by_category[key] += expense.amount
        else:
            total_by_category[key] = expense.amount
    print("Expense by Category: ")
    for key, amount in total_by_category.items():
        print(f" {key}: £{amount:.2f}")

    # calculate total expense
    total_expense = sum([expense.amount for expense in expenses])
    print(f"You have total spent £{total_expense} in this month!")

    # remanining budget
    remainning_budget = budget - total_expense
    if remainning_budget < 0:
        print(f"You have over spent £{abs(remainning_budget)} for this month!")
    elif remainning_budget > 0:
        print(f"You have left £{remainning_budget} for this month!")
    else:
        print(daily_budget)

    # Get the current date
    now = datetime.datetime.now()

    # Get the number of days in the current month
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    
    # calculate the remaining of days in the current month
    remaining_days = days_in_month - now.day
    print("Remaining days in the current month:", remaining_days)

    daily_budget = remainning_budget / remaining_days
    if daily_budget > 0:
        print(f"You can only spent £{daily_budget:.2f} in a day!")
    else:
        print("You are over the budget for a month!")


if __name__ == "__main__":
    main()
