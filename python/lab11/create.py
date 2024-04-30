#Bu dosya, bir PostgreSQL veritabanında bir tablo oluşturmayı, varsa tabloyu silmeyi ve
#ardından Phone_book adında bir tablo oluşturmayı sağlar.
# Bu tablo, telefon numarası, ad ve soyadı sütunlarına sahip bir telefon rehberi olarak tasarlanmıştır.


import psycopg2

connection = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234"
)

create_phonebook_table = '''
    CREATE TABLE IF NOT EXISTS Phone_book(
        PHONE_NUMBER TEXT PRIMARY KEY NOT NULL,
        NAME TEXT,
        SURNAME TEXT
    )
'''

cursor = connection.cursor()

# Tablonun varlığını kontrol et
cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'phone_book')")
table_exists = cursor.fetchone()[0]

# Eğer tablo varsa, sil
if table_exists:
    cursor.execute('DROP TABLE Phone_book')
    print('Table dropped')

# Tabloyu oluştur
try:
    cursor.execute(create_phonebook_table)
    connection.commit()
    print('Table created')
except Exception as error:
    print(f'Error: {error}')

connection.close()

