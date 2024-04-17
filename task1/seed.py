import psycopg2

from faker import Faker

conn = psycopg2.connect(dbname='postgres', user='postgres', password='password', host='localhost')
cursor = conn.cursor()

faker = Faker()

print("Users:")
for _ in range(25):
    fullname = faker.name()
    email = faker.email()
    print(f"{fullname:50} : {email}")
    cursor.execute(
        "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

conn.commit()

print("Tasks:")
for _ in range(100):
    title = faker.sentence()
    description = faker.text()
    status_id = faker.random_int(min=1, max=3)
    user_id = faker.random_int(min=1, max=25)
    print(f"{title}:\n\t{description}\n\t{status_id}n\t{user_id}")
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                   (title, description, status_id, user_id))

conn.commit()
cursor.close()
conn.close()