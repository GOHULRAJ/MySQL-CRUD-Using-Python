import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="testdatabase",
    port="3306"
)

mycursor=mydb.cursor()

mycursor.execute("SHOW TABLES")

for db in mycursor:
    print(db)