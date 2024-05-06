import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

# Common parent directory
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_DIR / Path(path)


def run_gui_script():
    script_path = CURRENT_DIR.parent / "graphmenu" / "gui.py"
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
    640.0,
    62.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui_script,  # Modified command to run the gui.py script
    relief="flat"
)
button_1.place(
    x=92.0,
    y=205.0,
    width=502.40386962890625,
    height=110.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=709.0,
    y=205.0,
    width=485.9223327636719,
    height=110.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=82.0,
    y=360.0,
    width=510,
    height=110.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=700.0,
    y=360.0,
    width=495.0,
    height=110.0
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
    x=299.0,
    y=535.0,
    width=680,
    height=110.0
)

window.resizable(False, False)
window.mainloop()
