import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from src.monthly_budget import left_to_spend, load_data, save_data, view_log_file, set_monthly_budget, view_monthly_budget, remove_monthly_budget
from expense import Expense
import main
import os
import unittest
from unittest.mock import patch
from datetime import datetime
from src.expense import Expense
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

    import src.monthly_budget as monthly_budget
    monthly_data = tmp_path / "monthly_budget_data.json"
    log_file = tmp_path / "monthly_budget_log.json"
    monkeypatch.setattr(monthly_budget, "monthly_data", str(monthly_data))
    monkeypatch.setattr(monthly_budget, "log_file", str(log_file))

def test_view_log_file(isolated_files):
    # Check error prevention
    log_file = ' '
    result = view_log_file()
    assert not os.path.exists(log_file)
    
    log_file = 'monthly_budget_log.json'
    assert os.path.exists(log_file)
    
    result = view_log_file()
    assert result == "Unfortunately, the log file does not exist."


    # Read and verify log content
    initial_budget = 1000
    data = load_data()
    data['monthly_budget'] = initial_budget
    save_data(data)
    with open(log_file, 'r') as file:
        log_data = json.load(file)
        assert isinstance(log_data, list)
        assert len(log_data) > 0 
        assert 'timestamp' in log_data[0]

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

def test_monthly_budget_functions(monkeypatch, capsys, isolated_files):
    # Test set monthly budget
    monkeypatch.setattr("builtins.input", lambda _: "1500")
    set_monthly_budget()
    data = load_data()
    assert data["monthly_budget"] == 1500

    # Test view monthly budget
    view_monthly_budget()
    captured = capsys.readouterr()
    assert "Monthly budget set to $1500.00" in captured.out
    
    # Test update monthly budget
    # Negative budget
    monkeypatch.setattr("builtins.input", lambda _: "-500")
    set_monthly_budget()
    captured = capsys.readouterr()
    assert "Error: Budget cannot be negative." in captured.out

    # Positive budget
    monkeypatch.setattr("builtins.input", lambda _: "2000")
    set_monthly_budget()
    captured = capsys.readouterr()
    assert "Monthly budget set to $2000.00" in captured.out
    
    # Test remove monthly budget
    # Non-zero budget
    remove_monthly_budget()
    captured = capsys.readouterr()
    assert "Monthly budget has been removed." in captured.out

    # Zero budget
    data = load_data()
    data['monthly_budget'] = 0
    save_data(data)
    remove_monthly_budget()
    captured = capsys.readouterr()
    assert "No monthly budget set currently." in captured.out
    
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
        Expected result: The monthly budget is successfully reset to 0.Add commentMore actions
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
    

 
