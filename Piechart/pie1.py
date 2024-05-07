import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("PSL.csv")

# Convert the 'dates' column to datetime format
df['dates'] = pd.to_datetime(df['dates'], errors='coerce')

# Sort the DataFrame by the date of the matches
df = df.sort_values(by='dates')

# Group the DataFrame by season and find the last match of each season
last_matches = df.groupby('season').tail(1)

# Get the winner of the last match of each season
season_winners = last_matches['Winner']

# Count the number of seasons won by each team
seasons_won_count = season_winners.value_counts()

# Define custom colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Explode the slices


# Plotting a pie chart with customizations
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.pie(seasons_won_count, labels=seasons_won_count.index, autopct='%1.1f%%', startangle=140, colors=colors, shadow=True)
plt.title('PSL Seasons Won by Teams', fontsize=25, fontweight='bold',pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()  # Adjust layout to prevent labels from being cut off
plt.show()
