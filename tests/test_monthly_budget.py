import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
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
