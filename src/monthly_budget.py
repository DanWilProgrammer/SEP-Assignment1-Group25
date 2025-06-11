import json
import os 
import plotly.express as px

monthly_data = 'monthly_budget_data.json'
log_file = 'monthly_budget_log.json'

def left_to_spend():
    # Send to output the remaining sum of money for the user to spend
    data = load_data()
    budget = data.get('monthly_budget', 0)
    total_expenses = sum(data.get('expenses', 0).values())  # Operation should be replaced by the total expenses function
    remaining_money = budget - total_expenses 
    return remaining_money

def load_data():
    # Load the budget data from a JSON file
    if not os.path.exists(monthly_data):
        return []
    with open(monthly_data, 'r') as file:
        return json.load(file)

def save_data(data):
    # Save the budget data to a JSON file
    with open(monthly_data, 'w') as file:
        json.dump(data, file, indent=4)
    with open(log_file, 'a') as file:
        json.dump(data, file, indent=4)

def log_file():
    # Present to user their log file with all of the months; Sends message to be print otherwise
    if not os.path.exists(log_file):
        return "Unfortunately, the log file does not exist. Please create a budget first."
    with open(log_file, 'r') as file:
       return json.load(file)

def set_monthly_budget():
    # Set the monthly budget based on user input
    try:
        amount = float(input("Set your monthly budget: $"))
        if amount < 0:
            raise ValueError("Budget cannot be negative.")
        data = load_data()
        data['monthly_budget'] = amount
        save_data(data)
        print(f"Monthly budget set to ${amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

def view_monthly_budget():
    # Load the budget data and display the current monthly budget
    data = load_data()
    budget = data.get('monthly_budget', 0)
    print(f"Your current monthly budget is: ${budget:.2f}")

def update_monthly_budget():
    # Update the monthly budget by a specified amount
    try:
        delta = float(input("Update budget by amount (+/-): $"))
        data = load_data()
        new_budget = data.get('monthly_budget', 0) + delta
        if new_budget < 0:
            raise ValueError("Resulting budget cannot be negative.")
        data['monthly_budget'] = new_budget
        save_data(data)
        print(f"Monthly budget updated to ${new_budget:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def remove_monthly_budget():
    data = load_data()
    if 'monthly_budget' in data:
        data['monthly_budget'] = 0
        save_data(data)
        print("Monthly budget has been removed.")
    else:
        print("No monthly budget set currently.")

def add_category():
    category_name = input("Enter the new category name: ").strip()
    if not category_name:
        print("Category name cannot be empty.")
        return

    data = load_data()
    categories = data.get('categories', [])
    if category_name not in categories:
        categories.append(category_name)
        data['categories'] = categories
        save_data(data)
        print(f"Category '{category_name}' added.")
    else:
        print(f"Category '{category_name}' already exists.")

def output_chart():
    # Generate a chart of expenses using Plotly
    data = load_data()
    expenses = data.get('expenses', {})

    if not expenses:
        print("No expenses recorded to chart.")
        return

    chart_type = input("Choose chart type (pie/bar): ").strip().lower()

    if chart_type == "pie":
        fig = px.pie(names=list(expenses.keys()), values=list(expenses.values()), title="Expense Breakdown (Pie Chart)")
    elif chart_type == "bar":
        fig = px.bar(x=list(expenses.keys()), y=list(expenses.values()), title="Expense Breakdown (Bar Chart)",
                     labels={'x': 'Category', 'y': 'Amount ($)'})
    else:
        print("Invalid chart type.")
        return

    file_name = "budget_chart.html"
    fig.write_html(file_name, auto_open=True)
    print(f"Chart opened in browser: {file_name}")

"""

Some ideas on how to possibly implement the input function as per this file

def menu():
    while True:
        print("\n--- Monthly Budget Menu ---")
        print("1. Set Monthly Budget")
        print("2. Update Monthly Budget")
        print("3. Remove Monthly Budget") # New option
        print("4. Add Category") # New option
        print("5. Output Chart")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            set_monthly_budget()
        elif choice == "2":
            update_monthly_budget()
        elif choice == "3":
            remove_monthly_budget()
        elif choice == "4":
            add_category()
        elif choice == "5":
            output_chart()
        elif choice == "6":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
"""
