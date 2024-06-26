
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
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
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "1.py"
    subprocess.Popen(['python', str(script_path)])
def run_gui_script2():
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "2.py"
    subprocess.Popen(['python', str(script_path)])
def run_gui_script3():
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "3.py"
    subprocess.Popen(['python', str(script_path)])
def run_gui_script4():
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "4.py"
    subprocess.Popen(['python', str(script_path)])
def run_gui_script5():
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "5.py"
    subprocess.Popen(['python', str(script_path)])
def run_gui_script6():
    script_path = CURRENT_DIR.parent.parent / "StatisticalMethods" / "6.py"
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
    79.0,
    image=image_image_1
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
    x=163.0,
    y=147.0,
    width=953.0,
    height=79.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script2,
    relief="flat"
)
button_3.place(
    x=143.0,
    y=243.0,
    width=993.0,
    height=77.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script3,
    relief="flat"
)
button_4.place(
    x=307.0,
    y=332.0,
    width=665.0,
    height=92.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script4,
    relief="flat"
)
button_5.place(
    x=305.0,
    y=436.0,
    width=666.0,
    height=87.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script5,
    relief="flat"
)
button_6.place(
    x=309.0,
    y=533.0,
    width=662.0,
    height=91.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script6,
    relief="flat"
)
button_7.place(
    x=501.0,
    y=633.0,
    width=278.0,
    height=78.0
)
window.resizable(False, False)
window.mainloop()
