# Personal Expenses Tracker

## Overview

![Personal Expenses Tracker image](assets/READMEfile/Responsive.jpg)

[Open Personal Expenses Tracker Program](https://iris-expense-tracker-2543ace1d062.herokuapp.com/)

## Personal Expenses Tracker
To make it easier to track daily expenses and understand your cash flow, this program shows how much money you've spent in each category and how much is left in your budget.

[Back to top](#personal-expenses-tracker)

## UX
### Ideal User Demographic
 
 The ideal user for this program is:

   - Anyone who wants to save money
   - Track their cash flow
   - Keep an eye on their expenses

### User-Stories

### Goals

   - Take charge of your finances and keep track of your expenses
   - allows you to categorize your expenses and easily identify where your money is going
   - Give daily spending limit feature, you can ensure that you're staying on budget and making the most of your money. 

### Development-Plan

![Plan](assets/READMEfile/Personalexpensetrackerplan.jpg)

# Feature
### How to use
  - Follow the instructions and input the name that you spent on.
  - Give it a cost of the item that you spent with.
  - Select the relevant category for the item that you spent.

  ![Welcome message](assets/READMEfile/personalExpenseTracker.jpg)
  
## Existing Features
  - key in the name of the item that you spend.
  - key in the cost of the item.
  - choose the most relevant category.

  ![Existing Features](assets/READMEfile/personalExpenseTracker.jpg)

  - The tracker will input your expenses into the file
  - Show the total amount of each category
  - Calculate the total amount that you spent in a month
  - Calculate if you have overspent how much amount and the remaining days in a month
  - If you overspend will tell the user how much the user overspent

  ![Expense tracker](assets/READMEfile/fulltesting.jpg)

  - input validation and error-checking for selecting category is out of range or key in invalid data

  ![valid check](assets/READMEfile/invalidtest.jpg)

[Back to top](#personal-expenses-tracker)
## Future Features

- **Remove of the expense from list**
- **Add emoji to make it more fun**
- **User can input monthly budget**

[Back to top](#personal-expenses-tracker)
# Data Model


[Back to top](#personal-expenses-tracker)
# Testing
I have manually tested this project by doing the following:

  - Passed the code through a PEP8 inter and confirmed there are no problems, only in line 83 is too long

  ![PEP8 Testing](assets/READMEfile/PEP8checker.jpg)

  - Given invalid inputs: strings when selecting categories, or number is not in the range.

  ![invalid testing](assets/READMEfile/invalidtest.jpg)

  - Tested in my local terminal and the Code institue Heroku terminal

  ![Heroku testing](assets/READMEfile/Herokutesting.jpg)

[Back to top](#personal-expenses-tracker)
# Bugs
## Solved Bugs

  - The range of selecting category is from (0,5) because in pythin the first number is from 0, I forgot to put the *value_range* is from 1. I fixed by add 1 to the *value_range* so when user select the range will only whitin 1-5.

  ![Bug 1](assets/READMEfile/bug_01_range_of_expense_value.jpg)

  - I encountered an issue where the try and except statements are not showing when a string or number is out of range. Because I didn't add if statement. I fixed by adding If statemnet and able to solve the problem.

  ![Bug 2](assets/READMEfile/bug_03_valueerror_handle.jpg)

  - I encountered an issue where I wanted to try to print my expense, there is a series of number codes printed in the terminal. I finxed this by using *__ repr __* in the expense.py file and able to solve the issue.

  ![Bug 3](assets/READMEfile/error.jpg)

## Remaining Bugs



## Validator Testing

  - PEP8
    - No errors were returned from [pep8ci.herokuapp](https://pep8ci.herokuapp.com/)

    ![PEP8](assets/READMEfile/PEP8checker.jpg)
    
[Back to top](#personal-expenses-tracker)
# Deployment
This project was deployed using Code Institute's mock terminal for Heroku.
 - Steps for deployment:
   - After setting up you account in [Heroku](https://heroku.com/)
   - Select *New* in the personal page and *Create new app* from drop dwon menu.
   - Your App name must be unique, and then choose a region depend on your locations, and click *Create App*.
   - Selecting *setting* tab, and find *Config Vars*, and set the value of KEY to *PORT*, and the value to *8000* then select add.
   - Then go down to the Buildpacks, select *Add buildpack*, select *Python* and save changes, and Add one more buildpack select Node.js and save changes. The order of the buildpacks is important, **python** first then **Node.js** second.
    


[Back to top](#personal-expenses-tracker)
# Credits
 - Code Institute for the deployment terminal


[Back to top](#personal-expenses-tracker)

