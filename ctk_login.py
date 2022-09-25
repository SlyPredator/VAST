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


class App(customtkinter.CTk):

    WIDTH = 862
    HEIGHT = 519

    def __init__(self):
        super().__init__()

        self.title("VAST - Login")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol(
            "WM_DELETE_WINDOW", self.on_closing
        )  # call .on_closing() when app gets closed
        logo = itk.PhotoImage(Image.open(ASSETS_PATH / "bitmap.png"))
        self.call("wm", "iconphoto", self._w, logo)
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
            anchor=tkinter.CENTER,
        )
        self.label_text_1.grid(row=0, column=0, pady=20, padx=230)
        self.user_entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Username"
        )
        self.user_entry.grid(
            row=8, column=0, columnspan=1, pady=0, padx=20, sticky="we"
        )
        self.pwd_entry = customtkinter.CTkEntry(
            master=self.frame_right, width=120, placeholder_text="Password"
        )
        self.pwd_entry.grid(
            row=10, column=0, columnspan=1, pady=30, padx=20, sticky="we"
        )
        self.check_box_1 = customtkinter.CTkCheckBox(
            master=self.frame_right, text="CTkCheckBox"
        )
        self.check_box_1.grid(row=12, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(
            master=self.frame_right, text="CTkCheckBox"
        )
        self.check_box_2.grid(row=12, column=2, pady=10, padx=20, sticky="w")
        self.button_5 = customtkinter.CTkButton(
            master=self.frame_right,
            text="Sign in",
            border_width=2,  # <- custom border_width
            fg_color="blue",  # <- no fg_color
            command=self.button_event,
        )
        self.button_5.grid(row=16, column=2, columnspan=1, pady=20, padx=20, sticky="we")

    def button_event(self):
        print("Button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
