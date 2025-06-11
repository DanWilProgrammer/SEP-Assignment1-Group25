import hashlib
import json
import os
from expense.py import _generate_id

database_file = "database.json"

def get_database()
    with open(database_file, 'r') as file:
        return json.load(file)

def register(user, pwd)
    file = get_database()

    for username in file: 
        if username = user:
            return "Unfortunately, this username is already in use. Please choose another one."
 
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
    new_id = _generate_id()

    data = {
        "username": user,
        "password": hash_pwd,
        "unique_id": 
    }

    with open(database_file, 'a') as file:
        json.dump(data, file, indent=4)

def login(user, pwd)
    file = get_database()
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()

    for username in file: 
        if username = user and password = hash_pwd:
            return "Logged in successfully!" # not quite sure how the unique id works regarding the files

    return "Login failed :("

def input_expense() -> Expense:
    description = input("Enter expense description: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    category = input("Enter category (or press Enter for 'General'): ") or "General"
    return Expense(description, amount, category)

def main():
  
    new_expense = input_expense()
    expenses = [new_expense]
    print("Total expenses:", Expense.total_expenses(expenses))
    print("Average monthly expenses:", Expense.average_expenses(expenses))

if __name__ == "__main__":
    main()
