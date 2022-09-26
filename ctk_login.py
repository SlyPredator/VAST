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
        self.check_var1 = self.check_var2 = tkinter.IntVar(master=self.frame_right)

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
        self.check_box_1 = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Customer",
            onvalue="1",
            offvalue="0",
            command=self.checkbox_event1,
            variable=self.check_var1,
        )
        self.check_box_1.grid(row=4, column=0, pady=10, padx=100, sticky="we")

        self.check_box_2 = customtkinter.CTkCheckBox(
            master=self.frame_right,
            text="Admin",
            onvalue="1",
            offvalue="0",
            command=self.checkbox_event2,
            variable=self.check_var2,
        )
        # self.check_box_2.grid(row=4, column=1, pady=10, padx=20, sticky="s")
        self.check_box_2.place(x=400, y=225)
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

    def checkbox_event1(self):
        if self.check_var1.get() == 1:
            self.check_box_2.deselect()
    def checkbox_event2(self):
        if self.check_var2.get() == 1:
            self.check_box_1.deselect()    


if __name__ == "__main__":
    app = App()
    app.mainloop()
