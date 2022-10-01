import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="mydatabase"
)

mycursor = mydb.cursor()


def mcs():
    for x in mycursor:
        print(x)


def mycursor_fetch_cust():
    mycursor.execute("select * from customers")


def mycursor_fetch_admin():
    mycursor.execute("select * from admins")
