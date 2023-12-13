# The classes for the expenses to store our information
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    # provides the memory address of the object in hexadecimal form
    def __repr__(self):
        return f"Expense:({self.name}, {self.amount}, {self.category})"
