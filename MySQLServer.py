import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alx_book_store"
)

if mydb.is_connected():
    cursor = mydb.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
        
    cursor.close()

mydb.close()