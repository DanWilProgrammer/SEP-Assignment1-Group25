from expenses import Expense

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
