import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from expense import Expense
import main
import unittest
from datetime import datetime
from src.expense import Expense


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


class TestExpenseFunctions(unittest.TestCase):
    def setUp(self):
        self.exp1 = Expense("Lunch", 15.50, "romina", ["romina", "sanam"], "Food", datetime(2024, 5, 10))
        self.exp2 = Expense("Train", 30.00, "sanam", ["sanam"], "Transport", datetime(2024, 5, 15))
        self.exp3 = Expense("Groceries", 50.00, "romina", ["romina"], "Food", datetime(2024, 6, 5))
        self.exp4 = Expense("Cinema", 12.00, "sanam", ["romina", "sanam"], "Entertainment", datetime(2024, 6, 12))
        self.expenses = [self.exp1, self.exp2, self.exp3, self.exp4]

    def test_average_monthly_expenses_two_months(self):
        self.assertAlmostEqual(Expense.average_monthly_expenses(self.expenses), 53.75)

if __name__ == "__main__":
    unittest.main()
