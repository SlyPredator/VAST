import csv
import tkinter
import tkinter.messagebox
from pathlib import Path

import customtkinter
from PIL import Image
from PIL import ImageTk as itk
from tkintermapview import TkinterMapView

from libs.db_handler import *

ASSETS_PATH = Path(__file__).resolve().parents[1] / "assets"


class Login_App(customtkinter.CTk):

    WIDTH = 960
    HEIGHT = 519

    def __init__(self):
        super().__init__()

        self.title("VAST - Login")
        self.geometry(f"{Login_App.WIDTH}x{Login_App.HEIGHT}+290+120")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed
        logo = itk.PhotoImage(load_img("logo"))
        self.call("wm", "iconphoto", self._w, logo)
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=300, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # self.frame_left.configure(fg_color="#B9D0E9")
        self.frame_right.configure(fg_color="#B9D0E9")
        self.cust_check_var = self.admin_check_var = tkinter.IntVar(
            master=self.frame_right
        )
        self.custnum = self.adminnum = 0
        self.logged_in_cust = ""
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing
        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="VAST - Car Rentals",
            text_font=("Roboto Medium", -16),
        )  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10)
        self.label_info_1 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="If you love cars, but find it hard to identify \n"
            + "one which is perfect for you, VAST serves as an \n"
            + "interesting option. We make it possible for you to \n"
            + "pick your car based on your travelling needs.",
            height=100,
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.CENTER,
            text_font=("Roboto Medium", -14.5),
        )
        self.label_info_1.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
        self.label_info_2 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="Easy Steps to Start Driving our Rentals: \n\n"
            + "SIGN UP - In two minutes and get verified \n"
            + "CHOOSE - From our lineup and pay on-the-go \n"
            + "DRIVE - As simple as that. Enjoy driving!",
            height=130,
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.CENTER,
            text_font=("Roboto Medium", -14.5),
        )
        self.label_info_2.grid(column=0, row=2, sticky="nwe", padx=15, pady=15)
        self.label_text_1 = customtkinter.CTkLabel(
            master=self.frame_right,
            text="Enter the details",
            text_color="#0E2239",
            text_font=("Roboto Medium", -20),
        )
        self.label_text_1.grid(row=0, column=0, pady=20, padx=210, sticky="we")
        self.user_entry = customtkinter.CTkEntry(
            master=self.frame_right,
            width=120,
            placeholder_text="Username",
            text_font=("Roboto Medium", -16),
        )
        self.user_entry.grid(
            row=1, column=0, columnspan=1, pady=0, padx=40, sticky="we"
        )
        self.pwd_entry = customtkinter.CTkEntry(
            master=self.frame_right,
            width=120,
            placeholder_text="Password",
            text_font=("Roboto Medium", -16),
        )
        self.pwd_entry.grid(
            row=2, column=0, columnspan=1, pady=20, padx=40, sticky="we"
        )
        self.cust_checkbox = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Customer",
            onvalue="1",
            offvalue="0",
            command=self.cust_check_event,
            variable=self.cust_check_var,
            text_color="#0E2239",
            text_font=("Roboto Medium", -16),
        )
        self.cust_checkbox.grid(row=4, column=0, pady=10, padx=100, sticky="we")

        self.admin_checkbox = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Admin",
            onvalue="1",
            offvalue="0",
            command=self.admin_check_event,
            variable=self.admin_check_var,
            text_color="#0E2239",
            text_font=("Roboto Medium", -16),
        )
        # self.admin_checkbox.grid(row=4, column=1, pady=10, padx=20, sticky="s")
        self.admin_checkbox.place(x=370, y=225)
        self.sign_in_btn = customtkinter.CTkButton(
            master=self.frame_right,
            text="Sign in",
            border_width=2,  # <- custom border_width
            border_color="#0E2239",
            fg_color="#0E2239",  # <- no fg_color
            command=self.db_check,
            text_font=("Roboto Medium", -16),
        )
        self.sign_in_btn.grid(row=3, column=0, pady=10, padx=40, sticky="we")
        self.bind("<Return>", lambda event: self.db_check())
        self.register_label = tkinter.Label(
            master=self.frame_right,
            text="New here? Register by clicking here!",
            bg="#B9D0E9",  # 0D5F07
            fg="#0E2239",
            font=("Roboto Medium", int(12), "underline"),
            # text_font=("Roboto Medium", -16),
            # text_color="#0D5F07",
        )
        self.register_label.grid(row=5, column=0, pady=20, padx=20, sticky="nsew")
        self.register_label.bind("<Button-1>", self.register)
        self.resizable(False, False)

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def cust_check_event(self):
        if self.cust_check_var.get() == 1:
            self.admin_checkbox.deselect()
            self.custnum, self.adminnum = 1, 0
        else:
            self.custnum = 0

    def admin_check_event(self):
        if self.admin_check_var.get() == 1:
            self.cust_checkbox.deselect()
            self.custnum, self.adminnum = 0, 1
        else:
            self.adminnum = 0

    def register(self, event=0):
        app2 = Register_App(self)
        app2.grab_set()

    def customer_info(self, event=0):
        app3 = Car_Selector(self)
        app3.grab_set()

    def admin_open_map(self, event=0):
        app4 = Map_App(self)
        app4.grab_set()

    def db_check(self):
        if self.custnum == 0 or self.adminnum == 0:
            if self.custnum == 1:
                x = mycursor_fetch_any("customers")
                for record in x:
                    if record[1:] == (
                        self.user_entry.get().strip(),
                        self.pwd_entry.get().strip(),
                    ):
                        tkinter.messagebox.showinfo(message="Successfully logged in!")
                        mycursor.execute(
                            f"UPDATE logged SET name = '{self.user_entry.get()}'"
                        )
                        mydb.commit()
                        self.customer_info()
                        break
                else:
                    tkinter.messagebox.showerror(
                        message="Wrong credentials, try again!"
                    )
            elif self.adminnum == 1:
                x = mycursor_fetch_any("admins")
                for record in x:
                    if record == (
                        self.user_entry.get().strip(),
                        self.pwd_entry.get().strip(),
                    ):
                        tkinter.messagebox.showinfo(message="Successfully logged in!")
                        self.admin_open_map()
                        break
                else:
                    tkinter.messagebox.showerror(
                        message="Wrong credentials, try again!"
                    )
        if self.custnum == 0 and self.adminnum == 0:
            tkinter.messagebox.showerror(
                message="Select whether you're a customer or administrator!"
            )


class Register_App(customtkinter.CTkToplevel):

    WIDTH = 862
    HEIGHT = 519

    def __init__(self, parent):
        super().__init__(parent)

        self.title("VAST - Login")
        self.geometry(f"{Register_App.WIDTH}x{Register_App.HEIGHT}+290+120")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed
        logo = itk.PhotoImage(load_img("logo"))
        self.iconphoto(False, logo)
        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())
        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=300, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right.configure(fg_color="#2A6E6A")
        self.cust_check_var = self.admin_check_var = tkinter.IntVar(
            master=self.frame_right
        )

        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing
        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="VAST - Car Rentals",
            text_font=("Roboto Medium", -16),
        )  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10)
        self.label_info_1 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="CTkLabel: Lorem ipsum dolor sit,\n"
            + "amet consetetur sadipscing elitr,\n"
            + "sed diam nonumy eirmod tempor",
            height=100,
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.LEFT,
        )
        self.label_info_1.grid(column=0, row=4, sticky="nwe", padx=15, pady=15)
        self.label_text_1 = customtkinter.CTkLabel(
            master=self.frame_right,
            text="Enter the details",
            text_font=("Roboto Medium", -16),
        )
        self.label_text_1.grid(row=0, column=0, pady=20, padx=230, sticky="we")
        self.user_entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Username"
        )
        self.user_entry.grid(
            row=1, column=0, columnspan=1, pady=10, padx=20, sticky="we"
        )
        self.pwd_entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Password"
        )
        self.pwd_entry.grid(
            row=2, column=0, columnspan=1, pady=10, padx=20, sticky="we"
        )
        self.pwd_entry_confirm = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Re-enter password"
        )
        self.pwd_entry_confirm.grid(
            row=3, column=0, columnspan=1, pady=10, padx=20, sticky="nwse"
        )
        # self.cust_checkbox = customtkinter.CTkCheckBox(
        #     master=self.frame_right,
        #     text="Customer",
        #     onvalue="1",
        #     offvalue="0",
        #     command=self.cust_check_event,
        #     variable=self.cust_check_var,
        # )
        # self.cust_checkbox.grid(row=4, column=0, pady=10, padx=100, sticky="we")

        # self.admin_checkbox = customtkinter.CTkCheckBox(
        #     master=self.frame_right,
        #     text="Admin",
        #     onvalue="1",
        #     offvalue="0",
        #     command=self.admin_check_event,
        #     variable=self.admin_check_var,
        # )
        # # self.admin_checkbox.grid(row=4, column=1, pady=10, padx=20, sticky="s")
        # self.admin_checkbox.place(x=400, y=225)
        self.sign_up_btn = customtkinter.CTkButton(
            master=self.frame_right,
            text="Sign Up",
            border_width=2,  # <- custom border_width
            fg_color="blue",  # <- no fg_color
            command=self.db_write,
        )
        self.sign_up_btn.grid(row=4, column=0, pady=10, padx=20, sticky="we")
        self.bind("<Return>", lambda event: self.db_write())

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def cust_check_event(self):
        if self.cust_check_var.get() == 1:
            self.admin_checkbox.deselect()

    def admin_check_event(self):
        if self.admin_check_var.get() == 1:
            self.cust_checkbox.deselect()

    def db_write(self):
        self.detail_tup = (self.user_entry.get().strip(), self.pwd_entry.get().strip())
        mycursor.execute(
            f"INSERT INTO customers (username, password) VALUES {self.detail_tup}"
        )
        mydb.commit()
        tkinter.messagebox.showinfo(message="Successfully registered!")


class Map_App(customtkinter.CTkToplevel):

    MapApp_NAME = "TkinterMapView with CustomTkinter"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, parent):
        super().__init__(parent)

        self.title(Map_App.MapApp_NAME)
        self.geometry(str(Map_App.WIDTH) + "x" + str(Map_App.HEIGHT))
        self.minsize(Map_App.WIDTH, Map_App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand("tk::mac::Quit", self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=150, corner_radius=0, fg_color=None
        )
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(2, weight=1)

        self.button_1 = customtkinter.CTkButton(
            master=self.frame_left, text="Set Marker", command=self.set_marker_event
        )
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left,
            text="Clear Markers",
            command=self.clear_marker_event,
        )
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        self.map_label = customtkinter.CTkLabel(
            self.frame_left, text="Tile Server:", anchor="w"
        )
        self.map_label.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=["OpenStreetMap", "Google Normal", "Google Satellite"],
            command=self.change_map,
        )
        self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 0))

        self.MapAppearance_mode_label = customtkinter.CTkLabel(
            self.frame_left, text="MapAppearance Mode:", anchor="w"
        )
        self.MapAppearance_mode_label.grid(row=5, column=0, padx=(20, 20), pady=(20, 0))
        self.MapAppearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.frame_left,
            values=["Light", "Dark", "System"],
            command=self.change_MapAppearance_mode,
        )
        self.MapAppearance_mode_optionemenu.grid(
            row=6, column=0, padx=(20, 20), pady=(10, 20)
        )

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky="nswe",
            padx=(0, 0),
            pady=(0, 0),
        )

        self.entry = customtkinter.CTkEntry(
            master=self.frame_right, placeholder_text="Type Address"
        )
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(
            master=self.frame_right, text="Search", width=90, command=self.search_event
        )
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Bangalore")
        self.map_option_menu.set("Google Normal")
        self.MapAppearance_mode_optionemenu.set("Dark")

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())
        self.slider_1.set(self.map_widget.zoom)

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.MapAppend(
            self.map_widget.set_marker(current_position[0], current_position[1])
        )

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def change_MapAppearance_mode(self, new_MapAppearance_mode: str):
        customtkinter.set_MapAppearance_mode(new_MapAppearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server(
                "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
            )
        elif new_map == "Google normal":
            self.map_widget.set_tile_server(
                "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                max_zoom=22,
            )
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server(
                "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                max_zoom=22,
            )

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


class Customer_Page(customtkinter.CTkToplevel):
    WIDTH = 1016
    HEIGHT = 735

    def __init__(self, parent):
        super().__init__(parent)

        self.title("VAST - Customer Info")
        self.geometry(f"{Customer_Page.WIDTH}x{Customer_Page.HEIGHT}+250+30")
        logo = itk.PhotoImage(load_img("logo"))
        self.iconphoto(False, logo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=500, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # self.frame_left.configure(fg_color="#B9D0E9")
        self.frame_right.configure(fg_color="#B9D0E9")
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)
        self.user_image = itk.PhotoImage(load_img("user_image"))
        self.dummy_user_btn = customtkinter.CTkButton(
            master=self.frame_left,
            image=self.user_image,
            text="ㅤ",
            border_width=2,
            corner_radius=10,
            compound="top",
            border_color="#D35B58",
            fg_color=("gray84", "gray25"),
            hover_color=("gray84", "gray25"),
        )
        self.dummy_user_btn.grid(row=0, column=0, padx=20, pady=3)
        x = mycursor_fetch_any("logged")
        self.logged_in_cust = [record for record in x]
        self.user_label = customtkinter.CTkLabel(
            master=self.frame_left,
            text=self.logged_in_cust[0][0],
            text_font=("Roboto Medium", -13),
        )
        self.user_label.grid(row=1, column=0, padx=0, pady=0)


class Car_Selector(customtkinter.CTkToplevel):
    WIDTH = 1016
    HEIGHT = 735

    def __init__(self, parent):
        super().__init__(parent)

        self.title("VAST - Car Selector")
        self.geometry(f"{Customer_Page.WIDTH}x{Customer_Page.HEIGHT}+250+30")
        logo = itk.PhotoImage(load_img("logo"))
        self.iconphoto(False, logo)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=500, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # self.frame_left.configure(fg_color="#B9D0E9")
        self.frame_right.configure(fg_color="#B9D0E9")
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)
        self.user_image = itk.PhotoImage(load_img("user_image"))
        self.dummy_user_btn = customtkinter.CTkButton(
            master=self.frame_left,
            image=self.user_image,
            text="ㅤ",
            border_width=2,
            corner_radius=10,
            compound="top",
            border_color="#D35B58",
            fg_color=("gray84", "gray25"),
            hover_color=("gray84", "gray25"),
        )
        self.dummy_user_btn.grid(row=0, column=0, padx=20, pady=3)
        x = mycursor_fetch_any("logged")
        self.logged_in_cust = [record for record in x]
        self.user_label = customtkinter.CTkLabel(
            master=self.frame_left,
            text=self.logged_in_cust[0][0],
            text_font=("Roboto Medium", -13),
        )
        self.user_label.grid(row=1, column=0, padx=0, pady=0)
        self.myframe = customtkinter.CTkFrame(
            master=self.frame_right,
            width=500,
            height=100,
            bg_color="#B9D0E9",
            fg_color="#B9D0E9",
        )
        self.myframe.place(x=0, y=0)

        self.canvas = tkinter.Canvas(self.myframe, bg="#B9D0E9")
        self.frame = customtkinter.CTkFrame(
            self.canvas, bg_color="#B9D0E9", border_color="#B9D0E9", fg_color="#B9D0E9"
        )
        self.myscrollbar = customtkinter.CTkScrollbar(
            master=self.myframe,
            orientation="horizontal",
            command=self.canvas.xview,
            fg_color="#B9D0E9",
            height=50,
        )
        self.canvas.configure(xscrollcommand=self.myscrollbar.set)

        self.myscrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="left")
        self.canvas.create_window((50, 50), window=self.frame, anchor="w")
        self.frame.bind("<Configure>", self.myfunction)
        self.data()

    def myfunction(self, event):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all"),
            width=1000,
            height=790,
            bg="#B9D0E9",
            borderwidth=0,
        )

    def data(self):
        customtkinter.CTkLabel(
            text="SELECT YOUR CAR",
            height=50,
            corner_radius=10,  # <- custom corner radius
            fg_color=("white", "black"),  # <- custom tuple-color
            justify=tkinter.CENTER,
            text_font=("Roboto Medium", -14.5),
            bg_color="#B9D0E9"
        ).grid(row=0, column=1)
        self.car1 = itk.PhotoImage(Image.open(ASSETS_PATH / "tata_nexon.png"))
        self.car2 = itk.PhotoImage(Image.open(ASSETS_PATH / "nio_es8.png"))
        self.car3 = itk.PhotoImage(Image.open(ASSETS_PATH / "tesla_model_3.png"))
        customtkinter.CTkButton(
            master=self.frame,
            image=self.car1,
            text="TATA NEXON",
            border_width=2,
            corner_radius=10,
            compound="top",
            border_color="#D35B58",
            fg_color=("gray84", "gray25"),
            # hover_color=("gray84", "gray25"),
            command=self.button_event,
            # bg_color="#B9D0E9"
        ).grid(row=1, column=0, padx=20, pady=20)
        customtkinter.CTkButton(
            master=self.frame,
            image=self.car2,
            text="NIO ES8",
            border_width=2,
            corner_radius=10,
            compound="top",
            border_color="#D35B58",
            fg_color=("gray84", "gray25"),
            command=self.button_event,
            # hover_color=("gray84", "gray25"),
        ).grid(row=1, column=2, padx=20, pady=20)
        customtkinter.CTkButton(
            master=self.frame,
            image=self.car3,
            text="TESLA MODEL 3",
            border_width=2,
            corner_radius=10,
            compound="top",
            border_color="#D35B58",
            fg_color=("gray84", "gray25"),
            command=self.button_event,
            # hover_color=("gray84", "gray25"),
        ).grid(row=1, column=3, padx=20, pady=20)

    def button_event(self):
        print("Button pressed")
