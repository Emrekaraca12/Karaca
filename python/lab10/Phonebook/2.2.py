import psycopg2

#Veritabanı ile bağlantı kurun
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="1234"
)

# Veritabanı işlemlerini gerçekleştirmek için bir imleç açın
cur = conn.cursor()

# Çalışanlar tablosuna yeni bir çalışan eklemek için INSERT deyimini yürütün
Test = "INSERT INTO Phonebook (first_name, last_name, address, phone_number ) VALUES (%s, %s, %s, %s) RETURNING id;"

multy = "INSERT INTO Phonebook (first_name, last_name, address, phone_number )  VALUES (%s, %s, %s, %s);"

cur.execute(Test, ("First", "Second", "City", 23230))

# İşlemi tamamla
conn.commit()

# İmleci ve veritabanı bağlantısını kapat
cur.close()
conn.close()
