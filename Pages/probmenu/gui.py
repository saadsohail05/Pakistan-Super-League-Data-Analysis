
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Common parent directory
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_DIR / Path(path)


# Create the Tkinter window
window = Tk()
window.title("Pakistan Super League Data Analysis")
window.configure(bg="#000000")

# Calculate the center coordinates of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 1280
window_height = 720
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2) - 50  # Adjusting the y coordinate
print(x, y)

# Set the window size and position it a bit higher than the center of the screen
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
def run_gui_script():
    script_path = CURRENT_DIR.parent / "mainpage" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
def run_gui_script1():
    script_path = CURRENT_DIR.parent.parent / "Binomial" / "binomial-Distribution.py"
    subprocess.Popen(['python', str(script_path)])
   



canvas = Canvas(
    window,
    bg = "#282C35",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    639.0,
    87.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    639.0,
    257.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script,
    relief="flat"
)
button_1.place(
    x=15.0,
    y=8.0,
    width=51.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script1,
    relief="flat"
)
button_2.place(
    x=487.0,
    y=384.0,
    width=305.0,
    height=89.0
)
window.resizable(False, False)
window.mainloop()