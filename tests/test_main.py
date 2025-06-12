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

def test_duplicate_registration(isolated_files):
    user = "TestUser"
    pwd = "123"
    register(user, pwd)
    duplicate = register(user, "456")
    assert "already in use" in duplicate
    

