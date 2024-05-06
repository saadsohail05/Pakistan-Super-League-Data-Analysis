from tkinter import Tk, Canvas, Button, PhotoImage, OptionMenu, StringVar
from pathlib import Path

# Common parent directory
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_DIR / Path(path)

def on_dropdown_select(value):
    print("Selected option:", value)

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

# Your existing image and button code
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    655.0,
    95.0,
    image=image_image_1
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(x=15.0, y=8.0, width=51.0, height=51.0)

# Dropdown menu below image_1
options = ["Option 1", "Option 2", "Option 3"]  # Add your options here
selected_option = StringVar(window)
selected_option.set(options[0])  # Set default option
dropdown_menu = OptionMenu(window, selected_option, *options, command=on_dropdown_select)
dropdown_menu.configure(bg="#282C35", fg="white", bd=0, highlightthickness=0, relief="flat", activebackground="#3E4149", activeforeground="white")
dropdown_menu.place(x=655, y=180, anchor="center")

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    655.0,
    456.0,
    image=image_image_2
)

window.resizable(False, False)
window.mainloop()
