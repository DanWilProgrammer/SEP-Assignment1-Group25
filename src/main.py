import hashlib
import json
import os
from expense.py import _generate_id

database_file = "database.json"

def get_database()
    with open(database_file, 'r') as file:
        return json.load(file)

def register(user, pwd)
    file = get_database()

    for username in file: 
        if username = user:
            return "Unfortunately, this username is already in use. Please choose another one."
 
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()
    new_id = _generate_id()

    data = {
        "username": user,
        "password": hash_pwd,
        "unique_id": 
    }

    with open(database_file, 'a') as file:
        json.dump(data, file, indent=4)

def login(user, pwd)
    file = get_database()
    hash_pwd = hashlib.md5(pwd.encode()).hexdigest()

    for username in file: 
        if username = user and password = hash_pwd:
            return "Logged in successfully!" # not quite sure how the unique id works regarding the files

    return "Login failed :("

