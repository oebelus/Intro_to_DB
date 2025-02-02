import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="alx_book_store"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

mycursor.close()
mydb.close()