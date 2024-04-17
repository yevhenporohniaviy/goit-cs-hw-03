import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost')
cursor = conn.cursor()


def get_tasks_by_user_id(user_id):
    query = "SELECT * FROM tasks WHERE user_id = %s;"
    cursor.execute(query, (user_id,))
    print("\n\n", user_id, ":", cursor.fetchall())


def get_tasks_by_status(status):
    query = "SELECT tasks.* FROM tasks JOIN status ON tasks.status_id = status.id WHERE status.name = %s;"
    cursor.execute(query, (status,))
    print("\n\n", status, ":", cursor.fetchall())


def update_task_status(task_id, new_status):
    query = """
    UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = %s) WHERE id = %s;
    """
    cursor.execute(query, (new_status, task_id))
    conn.commit()
    print("\n\n", task_id, " -> ", new_status)


def get_users_without_tasks():
    query = "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);"
    cursor.execute(query)
    print("\n\n", "Users without tasks:", cursor.fetchall())


def add_task_for_user(user_id, title, description, status_name):
    query = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES (%s, %s, (SELECT id FROM status WHERE name = %s), %s);
    """
    cursor.execute(query, (title, description, status_name, user_id))
    conn.commit()
    print("\n\n", "Added a task for user", user_id)


def get_incomplete_tasks():
    query = "SELECT tasks.* FROM tasks JOIN status ON tasks.status_id = status.id WHERE status.name != 'completed';"
    cursor.execute(query)
    print("\n\n", "Incompleted tasks:", cursor.fetchall())


def delete_task(task_id):
    query = "DELETE FROM tasks WHERE id = %s;"
    cursor.execute(query, (task_id,))
    conn.commit()
    print("\n\n", f"Task {task_id} was deleted")


def find_users_by_email(email_pattern):
    query = "SELECT * FROM users WHERE email LIKE %s;"
    cursor.execute(query, (email_pattern,))
    print("\n\n", "Users with email like", email_pattern, ":", cursor.fetchall())


def update_user_name(user_id, new_name):
    query = "UPDATE users SET fullname = %s WHERE id = %s;"
    cursor.execute(query, (new_name, user_id))
    conn.commit()
    print("\n\n", "Updated user", user_id, "name to", new_name)


def get_task_count_by_status():
    query = "SELECT status.name, COUNT(tasks.id) FROM status LEFT JOIN tasks ON status.id = tasks.status_id GROUP BY status.name;"
    cursor.execute(query)
    print("\n\n", "Task count by status:", cursor.fetchall())


def get_tasks_for_email_domain(domain):
    query = "SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE %s;"
    cursor.execute(query, ('%' + domain,))
    print("\n\n", "Tasks for users with domain", domain, ":", cursor.fetchall())


def get_tasks_without_description():
    query = "SELECT * FROM tasks WHERE description IS NULL OR description = '';"
    cursor.execute(query)
    print("\n\n", "Tasks without description:", cursor.fetchall())


def get_users_with_tasks_in_progress():
    query = """
    SELECT users.*, tasks.* FROM users
    INNER JOIN tasks ON users.id = tasks.user_id
    INNER JOIN status ON tasks.status_id = status.id
    WHERE status.name = 'in progress';
    """
    cursor.execute(query)
    print("\n\n", "Users with tasks in progress:", cursor.fetchall())


def get_users_with_task_counts():
    query = "SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname;"
    cursor.execute(query)
    print("\n\n", "Users with task counts:", cursor.fetchall())


get_tasks_by_user_id(1)
get_tasks_by_status('new')
update_task_status(1, 'in progress')
get_users_without_tasks()
add_task_for_user(1, 'New Task Title', 'Task description here.', 'new')
get_incomplete_tasks()
delete_task(1)
find_users_by_email('%@example.com')
update_user_name(1, 'New Name')
get_task_count_by_status()
get_tasks_for_email_domain('example.com')
get_tasks_without_description()
get_users_with_tasks_in_progress()
get_users_with_task_counts()

cursor.close()
conn.close()