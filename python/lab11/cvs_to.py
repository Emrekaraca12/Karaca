#csv_to_mysql.py: Bu dosya, bir CSV dosyasından verileri okur
# ve bu verileri PostgreSQL veritabanındaki Phone_book tablosuna ekler.
import psycopg2
import pandas as pd

connection = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234"
)

data = pd.read_csv(r"C:\Users\gazie\Desktop\desktop\PP2\lab11\data.csv")


df = pd.DataFrame(data)

cursor = connection.cursor()

for row in df.itertuples():
    print(row.phone_number)
    cursor.execute(
        """
        INSERT INTO phone_book (phone_number, name, surname)
        VALUES (%s, %s, %s)
        """,
        [row.phone_number, row.name, row.surname]
    )

connection.commit()
