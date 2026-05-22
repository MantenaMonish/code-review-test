# src/user_service.py

def get_user(user_id):
    users = {1: "alice", 2: "bob"}
    return users.get(user_id)

def format_greeting(name):
    if not name:
        return "Hello, stranger"
    return f"Hello, {name}"

def delete_user(user_id):
    del user
    return flase
