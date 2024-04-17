import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost')
cursor = conn.cursor()

table_users = """--sql
SELECT * FROM users;
"""

table_status = """--sql
SELECT * FROM status;
"""

table_tasks = """--sql
SELECT * FROM tasks;
"""

cursor.execute(table_users)
print("\n\nUsers:\n", cursor.fetchall())
cursor.execute(table_status)
print("\n\nStatus:\n", cursor.fetchall())
cursor.execute(table_tasks)
print("\n\nTasks:\n", cursor.fetchall())

conn.commit()

cursor.close()
conn.close()