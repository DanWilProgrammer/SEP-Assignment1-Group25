import hashlib
import json
import os
from datetime import datetime
from expense import Expense
from monthly_budget import *

database_file = "database.json"
expenses_file = "user_expenses.json"
current_user = None

def initialize_files():
    """Initialize database files if they don't exist."""
    if not os.path.exists(database_file):
        with open(database_file, 'w') as file:
            json.dump({}, file)
    
    if not os.path.exists(expenses_file):
        with open(expenses_file, 'w') as file:
            json.dump({}, file)

def get_database():
    """Load user database."""
    try:
        with open(database_file, 'r') as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_database(data):
    """Save user database."""
    with open(database_file, 'w') as file:
        json.dump(data, file, indent=4)

def get_user_expenses():
    """Load user expenses."""
    try:
        with open(expenses_file, 'r') as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_user_expenses(data):
    """Save user expenses."""
    with open(expenses_file, 'w') as file:
        json.dump(data, file, indent=4)

def _generate_id():
    """Generate a unique ID."""
    return f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

def register(user, pwd):
    """Register a new user."""
    db = get_database()
    
    if user in db:
        return "Unfortunately, this username is already in use. Please choose another one."
    
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
    new_id = _generate_id()
    
    db[user] = {
        "password": hash_pwd,
        "unique_id": new_id
    }
    
    save_database(db)
    
    # Initialize user's expense list
    expenses_db = get_user_expenses()
    expenses_db[user] = []
    save_user_expenses(expenses_db)
    
    return f"User '{user}' registered successfully!"

def login(user, pwd):
    """Login a user."""
    global current_user
    db = get_database()
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
    
    if user in db and db[user]["password"] == hash_pwd:
        current_user = user
        return "Logged in successfully!"
    
    return "Login failed :("

def logout():
    """Logout current user."""
    global current_user
    current_user = None
    print("Logged out successfully!")

def input_expense():
    """Get expense input from user."""
    if not current_user:
        print("Please log in first!")
        return None
        
    description = input("Enter expense description: ")
    
    while True:
        try:
            amount = float(input("Enter amount: $"))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    category = input("Enter category (or press Enter for 'General'): ").strip() or "General"
    
    # For simplicity, using current user as payer and only participant
    participants = [current_user]
    
    # Ask if there are other participants
    while True:
        add_participant = input("Add another participant? (y/n): ").strip().lower()
        if add_participant == 'y':
            participant = input("Enter participant name: ").strip()
            if participant and participant not in participants:
                participants.append(participant)
        elif add_participant == 'n':
            break
        else:
            print("Please enter 'y' or 'n'")
    
    return Expense(description, amount, current_user, participants, category)

def add_expense():
    """Add expense to user's list."""
    expense = input_expense()
    if not expense:
        return
    
    expenses_db = get_user_expenses()
    if current_user not in expenses_db:
        expenses_db[current_user] = []
    
    expenses_db[current_user].append(expense.to_dict())
    save_user_expenses(expenses_db)
    print(f"Expense added: {expense}")

def view_expenses():
    """View user's expenses."""
    if not current_user:
        print("Please log in first!")
        return
    
    expenses_db = get_user_expenses()
    user_expenses_data = expenses_db.get(current_user, [])
    
    if not user_expenses_data:
        print("No expenses recorded.")
        return
    
    expenses = [Expense.from_dict(exp_data) for exp_data in user_expenses_data]
    
    print(f"\n--- Expenses for {current_user} ---")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense}")
    
    print(f"\nTotal expenses: ${Expense.total_expenses(expenses):.2f}")
    print(f"Average monthly expenses: ${Expense.average_monthly_expenses(expenses):.2f}")
    
    # Show expenses by category
    category_totals = Expense.total_expenses_per_category(expenses)
    print(f"\nExpenses by category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")

def auth_menu():
    """Authentication menu."""
    while True:
        print("\n--- Welcome to Expense Tracker ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if username and password:
                result = register(username, password)
                print(result)
            else:
                print("Username and password cannot be empty.")
                
        elif choice == "2":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if username and password:
                result = login(username, password)
                print(result)
                if "successfully" in result:
                    return True  # Login successful
            else:
                print("Username and password cannot be empty.")
                
        elif choice == "3":
            return False  # Exit
        else:
            print("Invalid option. Please try again.")

def expense_menu():
    """Main expense tracking menu."""
    while True:
        print(f"\n--- Expense Tracker - Welcome {current_user}! ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Budget Management")
        print("4. Logout")
        print("5. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            add_expense()
            
        elif choice == "2":
            view_expenses()
            
        elif choice == "3":
            budget_menu()
            
        elif choice == "4":
            logout()
            return True  # Return to auth menu
            
        elif choice == "5":
            return False  # Exit application
            
        else:
            print("Invalid option. Please try again.")

def budget_menu():
    """Monthly budget menu."""
    while True:
        print(f"\n--- Monthly Budget Menu - {current_user} ---")
        print("1. Set Monthly Budget")
        print("2. View Monthly Budget")
        print("3. Update Monthly Budget")
        print("4. Remove Monthly Budget")
        print("5. Add Category")
        print("6. View Remaining Budget")
        print("7. Output Chart")
        print("8. View Log File")
        print("9. Back to Main Menu")
        
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
            # Get user's expenses for budget calculation
            expenses_db = get_user_expenses()
            user_expenses_data = expenses_db.get(current_user, [])
            expenses = [Expense.from_dict(exp_data) for exp_data in user_expenses_data]
            remaining = left_to_spend(expenses)
            print(f"Remaining budget: ${remaining:.2f}")
        elif choice == "7":
            output_chart(current_user)
        elif choice == "8":
            log_result = view_log_file()
            print(log_result)
        elif choice == "9":
            break
        else:
            print("Invalid option. Please try again.")

def main():
    """Main application entry point."""
    initialize_files()
    
    print("Welcome to the Expense Tracker Application!")
    
    while True:
        if not current_user:
            # Show authentication menu
            continue_app = auth_menu()
            if not continue_app:
                break
        else:
            # Show main application menu
            continue_app = expense_menu()
            if not continue_app:
                break
    
    print("Thank you for using Expense Tracker!")

if __name__ == "__main__":
    main()
