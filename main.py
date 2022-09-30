import tkinter
import tkinter.messagebox
from pathlib import Path

import customtkinter
from PIL import Image
from PIL import ImageTk as itk

from window_classes import *

customtkinter.set_appearance_mode(
    "System"
)  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"

if __name__ == "__main__":
    app = Register_App()
    app.mainloop()
