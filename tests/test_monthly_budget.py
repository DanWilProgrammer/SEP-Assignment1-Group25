import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from src.monthly_budget import left_to_spend, load_data, save_data
from expense import Expense
import main
import unittest
from datetime import datetime
from src.expense import Expense
from unittest.mock import patch, mock_open
from monthly_budget import remove_monthly_budget
import os
import sys
import io

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

class TestRemoveMonthlyBudget(unittest.TestCase):

    def setUp(self):
        self.held_stdout = sys.stdout
        self.mock_stdout = io.StringIO()
        sys.stdout = self.mock_stdout

    def tearDown(self):
        sys.stdout = self.held_stdout

    @patch('monthly_budget.os.path.exists', return_value=True)
    @patch('monthly_budget.json.load')
    @patch('monthly_budget.json.dump')
    def test_RemoveMonthlyBudget_BudgetExists_BudgetIsZero(self, mock_json_dump, mock_json_load, mock_exists):
        """
        Tests: the functionality of remove_monthly_budget.
        Condition: An existing, non-zero monthly budget.
        Expected result: The monthly budget is successfully reset to 0.
        """
        initial_data = {
            "monthly_budget": 666.0,
            "expenses": {},
            "categories": ["Food"]
        }
        mock_json_load.return_value = initial_data

        mock_json_dump.side_effect = [
            None, 
            None  
        ]

        remove_monthly_budget()

        self.assertTrue(mock_json_dump.called, "json.dump should have been called to save data.")
        
        saved_data_monthly = mock_json_dump.call_args_list[0][0][0] 
        self.assertEqual(saved_data_monthly['monthly_budget'], 0, "In the saved data, monthly_budget should be 0 after calling the function.")

        self.assertIn("Monthly budget has been removed.", self.mock_stdout.getvalue())
