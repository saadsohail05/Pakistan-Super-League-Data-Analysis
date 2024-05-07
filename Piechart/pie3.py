import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("PSL.csv")

# Group the DataFrame by season
season_groups = df.groupby('season')

# Define colors for the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Iterate over each season
for season, season_df in season_groups:
    # Count the number of matches won by each team in the current season
    matches_won = season_df['Winner'].value_counts()
    
    # Get the team with the most wins in the current season
    team_with_most_wins = matches_won.idxmax()
    
    # Plot a pie chart for the current season
    plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
        # Center the plot window on the screen
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+{}+{}".format(128, 22))
    plt.pie(matches_won, labels=matches_won.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title(f'Teams with Most Matches Won in Season {season}', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.tight_layout()  # Adjust layout to prevent labels from being cut off
    plt.show()
