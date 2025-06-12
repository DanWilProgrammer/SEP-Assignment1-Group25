import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from expense import Expense
import main

def test_expense_save_and_load(isolated_files):
    user = "TestUser"
    pwd = "test123"
    register(user, pwd)
    login(user, pwd)

    # Create dummy expense
    expense = Expense("Test Expense", 100.0, user, [user], category="Food")
    
    data = get_user_expenses()
    data[user] = [expense.to_dict()]
    save_user_expenses(data)
    
    # Load back and verify
    loaded = get_user_expenses()
    assert user in loaded
    assert len(loaded[user]) == 1
    assert loaded[user][0]["amount"] == 100.0
    assert loaded[user][0]["category"] == "Food"
