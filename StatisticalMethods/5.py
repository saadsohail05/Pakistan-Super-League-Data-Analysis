import tkinter as tk
from tkinter import font
import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Calculating run rate
psl_data['Run Rate'] = psl_data['Total Runs'] / psl_data['Overs']

# Calculating variance of run rate per season
variance_run_rate_per_season = psl_data.groupby('season')['Run Rate'].var().reset_index()

# Function to open a Tkinter window and print the results
def print_results():
    root = tk.Tk()
    root.title("Variance of Run Rate per Season")
    root.configure(bg="#282c35")  # Set background color
    
    # Create a bold font for the heading
    heading_font = font.Font(family="Helvetica", size=16, weight="bold")
    # Create a font for the content
    content_font = font.Font(family="Helvetica", size=15)
    
    # Set resolution to 1280x720
    width = 1280
    height = 720
    
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate x and y position for centering the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set window size and position
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    # Create a label for the heading with bold font and modern look
    heading_label = tk.Label(root, text="Variance of Run Rate per Season:", bg="#282c35", fg="white", font=heading_font)
    heading_label.pack()
    
    # Print results in the Tkinter window
    for index, row in variance_run_rate_per_season.iterrows():
        season = row['season']
        variance = row['Run Rate']
        
        label_text = f"Season {season}:\n  Variance of Run Rate: {variance}"
        season_label = tk.Label(root, text=label_text, bg="#282c35", fg="white", font=content_font)
        season_label.pack()
    
    root.mainloop()

# Call the function to open the Tkinter window and print the results
print_results()
