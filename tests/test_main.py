import pytest
import json
from main import register, login, get_database, get_user_expenses, save_user_expenses, _generate_id
from expense import Expense
import main

@pytest.fixture
def isolated_files(tmp_path, monkeypatch):
    # Patch paths
    db_file = tmp_path / "database.json"
    exp_file = tmp_path / "user_expenses.json"
    db_file.write_text("{}")
    exp_file.write_text("{}")
    
    monkeypatch.setattr(main, "database_file", str(db_file))
    monkeypatch.setattr(main, "expenses_file", str(exp_file))
    
    return str(db_file), str(exp_file)

def test_register_and_login(isolated_files):
    user = "TestUser"
    pwd = "Secure123"

    # Register
    msg = register(user, pwd)
    assert "registered successfully" in msg

    # Login success
    login_msg = login(user, pwd)
    assert login_msg == "Logged in successfully!"

    # Login fail
    bad_login_msg = login(user, "wrongpass")
    assert bad_login_msg == "Login failed :("

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


