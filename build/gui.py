from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage, Label
from tkinter.ttk import Progressbar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\SaadS\Desktop\Psl Data Analysis\Pakistan-Super-League-Data-Analysis\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_progress(progress_bar, value):
    progress_bar['value'] = value
    progress_label.config(text=f"{value}%")
    window.update_idletasks()  # Update the window to display changes

def animate_loading(progress_bar, value=0):
    update_progress(progress_bar, value)
    if value < 100:
        window.after(50, animate_loading, progress_bar, value + 1)  # Increase value after 50 milliseconds

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

# Create canvas and other widgets
canvas = Canvas(window, bg="#FFFFFF", height=700, width=1280, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(640.0, 422.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(639.0, 123.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(640.0, 244.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(640.0, 244.0, image=image_image_4)

progress_bar = Progressbar(window, orient="horizontal", length=1280, mode="determinate")
progress_bar.place(x=0, y=700)

progress_label = Label(window, text="0%", font=("Arial", 12), bg="#FFDA1A")
progress_label.place(relx=0.5, rely=0.95, anchor="s")

# Start the loading animation
animate_loading(progress_bar)

# Make the window non-resizable
window.resizable(False, False)

# Start the Tkinter event loop
window.mainloop()
