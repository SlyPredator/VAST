import tkinter as tk
import tkinter.messagebox
from mapview import *
from PIL import ImageTk as itk, Image
from pathlib import Path

# import admin

# adwin = admin.adminpage1()

ASSETS_PATH = Path(__file__).resolve().parent / "assets"


def uwu():
    window.destroy()
    app = App()
    app.start()


def on_enter():
    global userlist
    userlist.clear()
    userlist.append(username.get())
    userlist.append(password.get())
    tk.messagebox.showinfo(title="User Details", message=userlist)


def admin_page(event):
    global admin_window
    admin_window = tk.Toplevel(window)
    admin_window.title("VAST - Login/Register - Admins")
    admin_window.geometry("862x519")
    canvas = tk.Canvas(
        admin_window,
        bg="#038c9e",
        height=519,
        width=862,
        bd=0,
        highlightthickness=0,
        relief="raised",
    )  # left rectangle
    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        431, 0, 431 + 431, 0 + 519, fill="#eeeeee", outline=""
    )  # right rectangle
    canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")
    # tb_img = ASSETS_PATH / "TextBox_Bg.png"
    text_box_bg = itk.PhotoImage(Image.open(ASSETS_PATH / "TextBox_Bg.png"))
    username_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
    password_img = canvas.create_image(650.5, 248.5, image=text_box_bg)

    username = tk.Entry(
        master=admin_window, background="#F6F7F9", bd=0, highlightthickness=0
    )
    username.place(x=490.0, y=139 + 25, width=321.0, height=35)
    # username.bind("<Tab>", on_enter); username.bind("<Return>", on_enter)
    username.focus()

    password = tk.Entry(
        master=admin_window, background="#F6F7F9", bd=0, highlightthickness=0
    )
    password.place(x=490.0, y=218 + 25, width=321.0, height=35)
    # password.bind("<Return>", on_enter)

    canvas.create_text(
        590,
        88.0,
        text="Enter the details",
        fill="#515486",
        font=("Arial-BoldMT", int(22.0)),
    )

    canvas.create_text(
        490.0,
        156.0,
        text="Username",
        fill="black",
        font=("Arial-BoldMT", int(13.0)),
        anchor="w",
    )
    canvas.create_text(
        490.0,
        234.5,
        text="Password",
        fill="black",
        font=("Arial-BoldMT", int(13.0)),
        anchor="w",
    )
    # car_img = tk.PhotoImage(file=ASSETS_PATH / "car_img2.gif")
    # canvas.create_image(40, 350, anchor="nw", image=car_img)

    title = tk.Label(
        master=admin_window,
        text="VAST",
        background="#038c9e",
        foreground="black",
        font=("Arial-BoldMT", int(30.0)),
    )
    title.place(x=90.0, y=90.0)

    info_text = tk.Label(
        master=admin_window,
        text="""Lorem ipsum dolor sit, amet 
    consectetur adipisicing elit. Dolorum 
    autem nisi officiis soluta in 
    accusamus quia similique aspernatur, 
    perferendis asperiores.""",
        background="#038c9e",
        foreground="white",
        justify="left",
        font=("Georgia", int(16.0)),
    )
    info_text.place(x=27.0, y=200.0)

    admin_label = tk.Label(text="Click here for admins")
    admin_label.place(x=588, y=400)
    admin_label.bind("<Button-1>")

    signin_btn_img = itk.PhotoImage(Image.open(ASSETS_PATH / "signin.png"))
    signin_btn = tk.Button(
        master=admin_window,
        image=signin_btn_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
    )
    signin_btn.place(x=570, y=300)

    admin_window.resizable(False, False)
    admin_window.mainloop()


global window
window = tk.Tk()
window.title("VAST - Login/Register")
logo = itk.PhotoImage(Image.open(ASSETS_PATH / "bitmap.png"))
window.call("wm", "iconphoto", window._w, logo)
window.geometry("862x519")
canvas = tk.Canvas(
    window,
    bg="#038c9e",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="raised",
)  # left rectangle
canvas.place(x=0, y=0)
canvas.create_rectangle(
    431, 0, 431 + 431, 0 + 519, fill="#eeeeee", outline=""
)  # right rectangle
canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")
text_box_bg = itk.PhotoImage(Image.open(ASSETS_PATH / "TextBox_Bg.png"))
username_img = canvas.create_image(650.5, 167.5, image=text_box_bg)
password_img = canvas.create_image(650.5, 248.5, image=text_box_bg)

userlist = []

username = tk.Entry(background="#F6F7F9", bd=0, highlightthickness=0)
username.place(x=490.0, y=139 + 25, width=321.0, height=35)
# username.bind("<Tab>", on_enter); username.bind("<Return>", on_enter)
username.focus()

password = tk.Entry(background="#F6F7F9", bd=0, highlightthickness=0)
password.place(x=490.0, y=218 + 25, width=321.0, height=35)
# password.bind("<Return>", on_enter)

canvas.create_text(
    490.0,
    156.0,
    text="Username",
    fill="black",
    font=("Arial-BoldMT", int(13.0)),
    anchor="w",
)
canvas.create_text(
    490.0,
    234.5,
    text="Password",
    fill="black",
    font=("Arial-BoldMT", int(13.0)),
    anchor="w",
)
# car_img = tk.PhotoImage(Image.open(ASSETS_PATH / "car_img2.gif"))
# canvas.create_image(40, 350, anchor="nw", image=car_img)

title = tk.Label(
    text="VAST",
    background="#038c9e",
    foreground="black",
    font=("Arial-BoldMT", int(30.0)),
)
title.place(x=90.0, y=90.0)

info_text = tk.Label(
    text="""Lorem ipsum dolor sit, amet 
consectetur adipisicing elit. Dolorum 
autem nisi officiis soluta in 
accusamus quia similique aspernatur, 
perferendis asperiores.""",
    background="#038c9e",
    foreground="white",
    justify="left",
    font=("Georgia", int(16.0)),
)
info_text.place(x=27.0, y=200.0)

admin_label = tk.Label(text="Click here for admins")
admin_label.place(x=588, y=400)
admin_label.bind("<Button-1>", admin_page)

signin_btn_img = itk.PhotoImage(Image.open(ASSETS_PATH / "signin.png"))
signin_btn = tk.Button(
    image=signin_btn_img,
    command=on_enter,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
)
signin_btn.place(x=570, y=300)

window.resizable(False, False)
window.mainloop()
