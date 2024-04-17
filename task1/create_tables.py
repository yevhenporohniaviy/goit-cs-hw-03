import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost')
cursor = conn.cursor()

create_table_users = """--sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_table_status = """--sql
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""

insert_into_status = """--sql
INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed');
"""

create_table_tasks = """--sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status(id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

cursor.execute(create_table_users)
cursor.execute(create_table_status)
cursor.execute(insert_into_status)
cursor.execute(create_table_tasks)

conn.commit()

cursor.close()
conn.close()