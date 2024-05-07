import tkinter as tk
from tkinter import font
from tkinter import ttk
import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Calculating the average target per season of every team
average_target_per_season = psl_data.groupby(['season', 'Team'])['Target Runs'].mean().reset_index()

# Calculating the median target per season of every team
median_target_per_season = psl_data.groupby(['season', 'Team'])['Target Runs'].median().reset_index()

# Calculating the mode target per season of every team
mode_target_per_season = psl_data.groupby(['season', 'Team'])['Target Runs'].apply(lambda x: x.mode()[0] if len(x.mode()) > 0 else None).reset_index()

# Merging the mean, median, and mode target per season
average_target_stats_per_season = pd.merge(average_target_per_season, median_target_per_season, on=['season', 'Team'], suffixes=('_mean', '_median'))
average_target_stats_per_season = pd.merge(average_target_stats_per_season, mode_target_per_season, on=['season', 'Team'])

# Function to open a Tkinter window and print the results
def print_results():
    root = tk.Tk()
    root.title("Average Target per Season of Every Team")
    root.configure(bg="#282c35")  # Set background color
    
    # Create a bold font for the heading
    heading_font = font.Font(family="Helvetica", size=16, weight="bold")
    # Create a font for the content
    content_font = font.Font(family="Helvetica", size=9)
    
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
    heading_label = tk.Label(root, text="Average Target per Season of Every Team:", bg="#282c35", fg="white", font=heading_font)
    heading_label.pack()
    
    # Create a Canvas widget with a scrollbar
    canvas = tk.Canvas(root, bg="#282c35", highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Create a frame to contain the labels
    frame = tk.Frame(canvas, bg="#282c35")
    canvas.create_window((0, 0), window=frame, anchor="nw")
    
    # Print results in the Tkinter window
    for season in average_target_stats_per_season['season'].unique():
        season_label = tk.Label(frame, text=f"Season {season}:", bg="#282c35", fg="white", font=content_font, justify="center")
        season_label.pack()
        
        season_data = average_target_stats_per_season[average_target_stats_per_season['season'] == season]
        for index, row in season_data.iterrows():
            team = row['Team']
            mean_target = row['Target Runs_mean']
            median_target = row['Target Runs_median']
            mode_target = row['Target Runs']
            
            team_label = tk.Label(frame, text=f"Team: {team}", bg="#282c35", fg="white", font=content_font, justify="center")
            team_label.pack()
            mean_label = tk.Label(frame, text=f"  Mean Target: {mean_target}", bg="#282c35", fg="white", font=content_font, justify="center")
            mean_label.pack()
            median_label = tk.Label(frame, text=f"  Median Target: {median_target}", bg="#282c35", fg="white", font=content_font, justify="center")
            median_label.pack()
            mode_label = tk.Label(frame, text=f"  Mode Target: {mode_target}", bg="#282c35", fg="white", font=content_font, justify="center")
            mode_label.pack()
    
    root.mainloop()

# Call the function to open the Tkinter window and print the results
print_results()
