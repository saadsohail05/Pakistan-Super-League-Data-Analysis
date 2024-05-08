import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

# Common parent directory
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_DIR / Path(path)


def run_gui_script():
    script_path = CURRENT_DIR.parent / "mainpage" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
    
def run_gui_script1():
    script_path = CURRENT_DIR.parent / "bargraphmenu" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
    
def run_gui_script2():
    script_path = CURRENT_DIR.parent / "linechartmenu" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
def run_gui_script3():
    script_path = CURRENT_DIR.parent / "histogrammenu" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
def run_gui_script3():
    script_path = CURRENT_DIR.parent / "fpmenu" / "gui.py"
    subprocess.Popen(['python', str(script_path)])
    window.destroy()
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

# Set the window size and position it a bit higher than the center of the screen
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

canvas = Canvas(
    window,
    bg="#282C35",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    639.0,
    145.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script3,
    relief="flat"
)
button_1.place(
    x=103.0,
    y=275.0,
    width=307.0,
    height=88.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script3,
    relief="flat"
)
button_2.place(
    x=463.0,
    y=275.0,
    width=393.0666809082031,
    height=88.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script1,
    relief="flat"
)
button_3.place(
    x=909.0,
    y=275.0,
    width=309.1891784667969,
    height=88.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script2,
    relief="flat"
)
button_4.place(
    x=315.0,
    y=500.0,
    width=296.0,
    height=88.0
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=660.0,
    y=500.0,
    width=303.8933410644531,
    height=88.0
)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script,  # Modified command to run the gui.py script
    relief="flat"
)
button_6.place(
    x=15.0,
    y=8.0,
    width=51.0,
    height=51.0
)

window.resizable(False, False)
window.mainloop()
