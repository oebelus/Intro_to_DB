import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alx_book_store"
)

if mydb.is_connected():
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully or already exists.")
    
    cursor.close()
    
mydb.close()