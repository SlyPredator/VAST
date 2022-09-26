import tkinter
import tkinter.messagebox
import customtkinter
from pathlib import Path
from PIL import ImageTk as itk, Image

ASSETS_PATH = Path(__file__).resolve().parent / "assets"


customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


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
        logo = itk.PhotoImage(Image.open(ASSETS_PATH / "bitmap.png"))
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
            +"interesting option. We make it possible for you to \n"
            +"pick your car based on your travelling needs.",
            height=100,
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.CENTER,
            text_font=("Roboto Medium", -14.5)
        )
        self.label_info_1.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
        self.label_info_2 = customtkinter.CTkLabel(
            master=self.frame_left,
            text="Easy Steps to Start Driving our Rentals: \n\n"
            + "SIGN UP - In two minutes and get verified \n"
            +"CHOOSE - From our lineup and pay on-the-go \n"
            +"DRIVE - As simple as that. Enjoy driving!",
            height=130,
            corner_radius=6,  # <- custom corner radius
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.CENTER,
            text_font=("Roboto Medium", -14.5)
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
            command=self.button_event,
            text_font=("Roboto Medium", -16),
        )
        self.sign_in_btn.grid(row=3, column=0, pady=10, padx=40, sticky="we")
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

    def admin_check_event(self):
        if self.admin_check_var.get() == 1:
            self.cust_checkbox.deselect()

    def register(self, event=0):
        app2 = Register_App()
        app2.mainloop()


class Register_App(customtkinter.CTk):

    WIDTH = 862
    HEIGHT = 519

    def __init__(self):
        super().__init__()

        self.title("VAST - Login")
        self.geometry(f"{Register_App.WIDTH}x{Register_App.HEIGHT}+290+120")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed
        logo2 = itk.PhotoImage(Image.open(ASSETS_PATH / "bitmap.png"))
        # self.call("wm", "iconphoto", self._w, logo2)
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
            row=1, column=0, columnspan=1, pady=0, padx=20, sticky="we"
        )
        self.pwd_entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Password"
        )
        self.pwd_entry.grid(
            row=2, column=0, columnspan=1, pady=20, padx=20, sticky="we"
        )
        self.cust_checkbox = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Customer",
            onvalue="1",
            offvalue="0",
            command=self.cust_check_event,
            variable=self.cust_check_var,
        )
        self.cust_checkbox.grid(row=4, column=0, pady=10, padx=100, sticky="we")

        self.admin_checkbox = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Admin",
            onvalue="1",
            offvalue="0",
            command=self.admin_check_event,
            variable=self.admin_check_var,
        )
        # self.admin_checkbox.grid(row=4, column=1, pady=10, padx=20, sticky="s")
        self.admin_checkbox.place(x=400, y=225)
        self.sign_in_btn = customtkinter.CTkButton(
            master=self.frame_right,
            text="Sign in",
            border_width=2,  # <- custom border_width
            fg_color="blue",  # <- no fg_color
            command=self.button_event,
        )
        self.sign_in_btn.grid(row=3, column=0, pady=10, padx=20, sticky="we")

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


if __name__ == "__main__":
    app = Login_App()
    app.mainloop()
