import sqlite3
import os

def valid_user_id(user_id):
    if len(user_id) == 0:
        return False

    for ch in user_id:
        if ch not in "0123456789":
            return False

    return True

def get_user(user_id):
    if not valid_user_id(user_id):
        return "Invalid user ID"

    if user_id == "1":
        return "This ID is not accepted"

    conn = sqlite3.connect(r"D:\Personal\Notes\Worlder\TASK2\users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", [user_id])
    data = cursor.fetchall()
    conn.close()

    return data

def readfile(filename):
    safedir = os.path.abspath("user_access")
    filepath = os.path.abspath(os.path.join(safedir, filename))

    if not filepath.startswith(safedir):
        return "Access denied"

    try:
        return open(filepath, "r").read()
    except:
        return "File not found"

user_id = input("Enter your user ID: ").strip()
print(get_user(user_id))

filename = input("Enter the file name: ").strip()
print(readfile(filename))




