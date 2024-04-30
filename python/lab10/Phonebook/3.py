# Implement updating data in the table (change user first name or phone)


import psycopg2

# Establish a connection to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",
    user="postgres",
    password="1234"
)

cur = conn.cursor()

# Execute an INSERT statement to add a new employee to the employees table


cur.execute("UPDATE PhoneBook SET first_name = %s,address= %s WHERE first_name = %s;",('ahmet','istanbul','First'))



# Commit the transaction
conn.commit()

# Close the cursor and database connection
cur.close()
conn.close()