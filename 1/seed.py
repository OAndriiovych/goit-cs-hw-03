from faker import Faker
import psycopg2
import random

conn = psycopg2.connect(
    dbname="hw3",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

fake = Faker()
count_of_users = 10

for _ in range(count_of_users):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()

statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))
    conn.commit()

for _ in range(20):
    title = fake.text(max_nb_chars=100)
    description = fake.text()
    status_id = random.randint(1, 3)
    user_id = random.randint(1, count_of_users)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))
    conn.commit()

cur.close()
conn.close()
