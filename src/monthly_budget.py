import json
import os 
from typing import List, Dict
import plotly.express as px
import plotly.graph_objects as go
        


monthly_data = 'monthly_budget_data.json'
log_file = 'monthly_budget_log.json'

def left_to_spend(expenses=None):
    """Send to output the remaining sum of money for the user to spend"""
    data = load_data()
    budget = data.get('monthly_budget', 0)
    
    if expenses:
        # Calculate from actual expenses if provided
        from expense import Expense
        total_expenses = Expense.total_expenses(expenses)
    else:
        # Use stored expenses data
        stored_expenses = data.get('expenses', {})
        total_expenses = sum(stored_expenses.values()) if isinstance(stored_expenses, dict) else 0
    
    remaining_money = budget - total_expenses 
    return remaining_money

def load_data():
    """Load the budget data from a JSON file"""
    if not os.path.exists(monthly_data):
        # Create default data structure
        default_data = {
            "monthly_budget": 0,
            "expenses": {},
            "categories": ["General", "Food", "Transportation", "Entertainment", "Utilities"]
        }
        save_data(default_data)
        return default_data
    
    try:
        with open(monthly_data, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        # Return default data if file is corrupted or missing
        return {
            "monthly_budget": 0,
            "expenses": {},
            "categories": ["General", "Food", "Transportation", "Entertainment", "Utilities"]
        }

def save_data(data):
    """Save the budget data to a JSON file"""
    with open(monthly_data, 'w') as file:
        json.dump(data, file, indent=4)
    
    # Also append to log file
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as file:
                log_data = json.load(file)
        else:
            log_data = []
        
        # Add timestamp to the data for logging
        log_entry = data.copy()
        from datetime import datetime
        log_entry['timestamp'] = datetime.now().isoformat()
        log_data.append(log_entry)
        
        with open(log_file, 'w') as file:
            json.dump(log_data, file, indent=4)
    except Exception as e:
        print(f"Warning: Could not update log file: {e}")

def view_log_file():
    """Present to user their log file with all of the months; Sends message to be print otherwise"""
    if not os.path.exists(log_file):
        return "Unfortunately, the log file does not exist. Please create a budget first."
    
    try:
        with open(log_file, 'r') as file:
            log_data = json.load(file)
        
        if not log_data:
            return "Log file is empty."
        
        result = "=== Budget History ===\n"
        for i, entry in enumerate(log_data, 1):
            timestamp = entry.get('timestamp', 'Unknown time')
            budget = entry.get('monthly_budget', 0)
            result += f"{i}. {timestamp}: Budget set to ${budget:.2f}\n"
        
        return result
    except Exception as e:
        return f"Error reading log file: {e}"

def set_monthly_budget():
    """Set the monthly budget based on user input"""
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
    """Load the budget data and display the current monthly budget"""
    data = load_data()
    budget = data.get('monthly_budget', 0)
    print(f"Your current monthly budget is: ${budget:.2f}")

def update_monthly_budget():
    """Update the monthly budget by a specified amount"""
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
    """Remove/reset the monthly budget"""
    data = load_data()
    if data.get('monthly_budget', 0) > 0:
        data['monthly_budget'] = 0
        save_data(data)
        print("Monthly budget has been removed.")
    else:
        print("No monthly budget set currently.")

def add_category():
    """Add a new expense category"""
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

def output_chart(current_user: str):
    """Generate a chart of user expenses using Plotly"""
    from expense import Expense
    from main import get_user_expenses

    try:
        import pandas as pd
        import plotly.express as px
    except ImportError:
        print("Missing required packages. Please run: pip install pandas plotly")
        return

    if not current_user:
        print("Please log in first!")
        return

    user_expenses_data = get_user_expenses().get(current_user, [])
    if not user_expenses_data:
        print("No expenses recorded to chart.")
        return

    expenses = [Expense.from_dict(exp) for exp in user_expenses_data]
    category_totals = Expense.total_expenses_per_category(expenses)

    chart_type = input("Choose chart type (pie/bar): ").strip().lower()

    # Convert to DataFrame
    df = pd.DataFrame({
        "Category": list(category_totals.keys()),
        "Amount": list(category_totals.values())
    })

    try:
        if chart_type == "pie":
            fig = px.pie(df, names="Category", values="Amount",
                         title="Expense Breakdown by Category (Pie Chart)")
        elif chart_type == "bar":
            fig = px.bar(df, x="Category", y="Amount",
                         title="Expense Breakdown by Category (Bar Chart)",
                         labels={"Category": "Category", "Amount": "Amount ($)"})
        else:
            print("Invalid chart type.")
            return

        file_name = "budget_chart.html"
        fig.write_html(file_name, auto_open=True)
        print(f"Chart saved and opened in browser: {file_name}")

    except Exception as e:
        print(f"Error generating chart: {e}")



def menu():
    """Standalone menu for budget management (can be used independently)"""
    while True:
        print("\n--- Monthly Budget Menu ---")
        print("1. Set Monthly Budget")
        print("2. View Monthly Budget")
        print("3. Update Monthly Budget")
        print("4. Remove Monthly Budget")
        print("5. Add Category")
        print("6. View Remaining Budget")  
        print("7. Output Chart")
        print("8. View Log File")
        print("9. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            set_monthly_budget()
        elif choice == "2":
            view_monthly_budget()
        elif choice == "3":
            update_monthly_budget()
        elif choice == "4":
            remove_monthly_budget()
        elif choice == "5":
            add_category()
        elif choice == "6":
            remaining = left_to_spend()
            print(f"Remaining budget: ${remaining:.2f}")
        elif choice == "7":
            output_chart()
        elif choice == "8":
            result = view_log_file()
            print(result)
        elif choice == "9":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
