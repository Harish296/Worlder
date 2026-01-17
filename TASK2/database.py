import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS users")

cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, device TEXT)")

cursor.execute("INSERT INTO users VALUES (1, 'Admin', 'Legacy System')")
cursor.execute("INSERT INTO users VALUES (2, 'Bob', 'Lenovo Legion')")
cursor.execute("INSERT INTO users VALUES (3, 'Mark', 'Mac')")
cursor.execute("INSERT INTO users VALUES (4, 'Peter', 'Dell G15')")
cursor.execute("INSERT INTO users VALUES (5, 'John', 'Acer Nitro')")
cursor.execute("INSERT INTO users VALUES (6, 'Alice', 'Hp Omen')")

conn.commit()
conn.close()


