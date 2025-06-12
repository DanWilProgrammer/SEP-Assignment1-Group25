import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from src.monthly_budget import left_to_spend, load_data, save_data
from expense import Expense
import main
import unittest
from datetime import datetime
from src.expense import Expense

@pytest.fixture
def isolated_files(tmp_path, monkeypatch):
    # Patch paths
    db_file = tmp_path / "database.json"
    exp_file = tmp_path / "user_expenses.json"
    db_file.write_text("{}")
    exp_file.write_text("{}")
    
    monkeypatch.setattr(main, "database_file", str(db_file))
    monkeypatch.setattr(main, "expenses_file", str(exp_file))

def test_left_to_spend(isolated_files):
    initial_budget = 1000
    data = load_data()
    data['monthly_budget'] = initial_budget
    save_data(data)
    
    # No expenses
    remaining = left_to_spend()
    assert remaining == initial_budget
    
    # Initial expenses
    expenses = [
        Expense(description="Food", amount=200, payer="User1", participants=["User1"]),
        Expense(description="Utilities", amount=150, payer="User1", participants=["User1"]),
    ]
    
    remaining = left_to_spend(expenses)
    assert remaining == initial_budget - 350
    
    # Add expenses
    expenses.append(Expense(description="Entertainment", amount=100, payer="User1", participants=["User1"]))
    
    remaining = left_to_spend(expenses)
    assert remaining == initial_budget - 450
