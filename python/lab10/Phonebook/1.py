import psycopg2
import csv

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234"
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE Phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        address VARCHAR(100),
        phone_number VARCHAR(15)
    )
""")

conn.commit()

cur.close()
conn.close()


