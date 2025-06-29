from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Label
from tkinter.ttk import Progressbar
import subprocess
import os

# Define paths
CURRENT_DIR = Path(__file__).parent
ASSETS_DIR = CURRENT_DIR / "assets"/"frame0"  # Assuming assets are in a directory named "assets" within the same directory as the script

# Function to get relative path to assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_DIR / Path(path)

# Function to update progress
def update_progress(progress_bar, value):
    progress_bar['value'] = value
    progress_label.config(text=f"{value}%")
    window.update_idletasks()  # Update the window to display changes

# Function to animate loading
def animate_loading(progress_bar, value=0):
    update_progress(progress_bar, value)
    if value < 100:
        window.after(50, animate_loading, progress_bar, value + 1)  # Increase value after 50 milliseconds
    else:
        # Loading completed, now execute another script
        execute_another_script()

# Function to execute another script
def execute_another_script():
    # Path to the script to be executed
    script_path = CURRENT_DIR.parent / "Pages" / "mainpage" / "gui.py"
    print(script_path)
    window.destroy()  # Close the current window
    subprocess.Popen(['python', str(script_path)])

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
print(x,y)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

# Load images onto canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    646.0,
    452.0,
    image=image_image_2
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    627.0,
    574.0,
    image=image_image_3
)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    627.0,
    574.0,
    image=image_image_4
)

# Create progress bar
progress_bar = Progressbar(window, orient="horizontal", length=1280, mode="determinate")
progress_bar.place(x=0, y=700)

# Create progress label
progress_label = Label(window, text="0%", font=("Arial", 12), bg="#FFDA1A")
progress_label.place(relx=0.5, rely=0.95, anchor="s")

# Start the loading animation
animate_loading(progress_bar)

# Make the window non-resizable
window.resizable(False, False)

# Start the Tkinter event loop
window.mainloop()
