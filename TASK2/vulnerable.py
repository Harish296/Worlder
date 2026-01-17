import sqlite3

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    conn = sqlite3.connect(r"D:\Personal\Notes\Worlder\TASK2\users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def readfile(filename):
    file = open("user_access/" + filename, "r")
    return file.read()

user_id = input("Enter user ID: ")
print(get_user(user_id)) 

filename = input("Enter file name: ")
print(readfile(filename))

