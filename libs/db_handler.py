import base64
import io
from pathlib import Path

import mysql.connector
from PIL import Image
from PIL import ImageTk as itk

password = open("password.txt").readline()
mydb = mysql.connector.connect(
    host="localhost", user="root", password=password, database="mydatabase"
)
ASSETS_PATH = Path(__file__).resolve().parents[1] / "assets"
mycursor = mydb.cursor()


def mcs():
    for x in mycursor:
        print(x)


def mycursor_fetch_any(name):
    mycursor.execute(f"select * from {name}")
    return mycursor.fetchall()


def dump_img(image_file, name):
    file = open(image_file, "rb").read()
    file = base64.b64encode(file)
    args = (name, file)
    query = "INSERT INTO pictures (NAME, PICTURE) VALUES(%s, %s)"
    mycursor.execute(query, args)
    mydb.commit()
    print("success")


def load_img(name: str):
    query = f"SELECT PICTURE FROM pictures WHERE NAME='{name}'"
    mycursor.execute(query)
    data = mycursor.fetchall()
    image = data[0][0]
    binary_data = base64.b64decode(image)
    image = Image.open(io.BytesIO(binary_data))
    return image


def chosen_car_img(username: str):
    query = f"SELECT car FROM customers WHERE username = '{username}'"
    mycursor.execute(query)
    data = mycursor.fetchall()
    car = data[0][0]
    return load_img(f"{car}")


# dump_img(ASSETS_PATH / "user_image.png", "user_image")
# load_img("user_image")
chosen_car_img("Tejas")
