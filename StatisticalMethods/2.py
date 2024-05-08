import tkinter as tk
from tkinter import font
import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Creating a new column to categorize overs
psl_data['Over_Category'] = pd.cut(psl_data['Over Number'], bins=[0, 6, 15, 20], labels=['Powerplay', 'Middle Overs', 'Death Overs'])

# Filtering out rows where a wicket fell
wickets_data = psl_data[psl_data['Wickets'] == 1]

# Counting the number of wickets per over category per season
wickets_per_season_over_category = wickets_data.groupby(['season', 'Over_Category'])['Wickets'].count().reset_index()

# Calculating total matches per season
matches_per_season = psl_data.groupby('season')['event match_number'].nunique().reset_index()

# Merging total wickets and total matches per season
average_wickets_per_season_over_category = pd.merge(wickets_per_season_over_category, matches_per_season, on='season')

# Calculating average wickets per over category per season
average_wickets_per_season_over_category['Average Wickets'] = average_wickets_per_season_over_category['Wickets'] / average_wickets_per_season_over_category['event match_number']

# Pivoting the table to get the desired format
average_wickets_per_season_over_category_pivot = average_wickets_per_season_over_category.pivot_table(index='season', columns='Over_Category', values='Average Wickets')

# Function to open a Tkinter window and print the results
def print_results():
    root = tk.Tk()
    root.title("Average Wickets of Teams")
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
    heading_label = tk.Label(root, text="Average Wickets of Teams in Powerplay, Middle Overs, and Death Overs per Season:", bg="#282c35", fg="white", font=heading_font)
    heading_label.pack()
    
    # Print results in the Tkinter window
    for season in average_wickets_per_season_over_category_pivot.index:
        powerplay_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Powerplay']
        middle_overs_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Middle Overs']
        death_overs_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Death Overs']
        
        label_text = f"Season {season}:\nPowerplay Average Wickets: {powerplay_avg}\nMiddle Overs Average Wickets: {middle_overs_avg}\nDeath Overs Average Wickets: {death_overs_avg}"
        season_label = tk.Label(root, text=label_text, bg="#282c35", fg="white", font=content_font)
        season_label.pack()
    
    root.mainloop()

# Call the function to open the Tkinter window and print the results
print_results()
