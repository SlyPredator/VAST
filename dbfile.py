import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mydatabase"
)

mycursor = mydb.cursor()

def mcs():
    for x in mycursor:
        print(x)

def mycursor_fetch():
    mycursor.execute("select * from customers")

