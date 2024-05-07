import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv("PSL.csv", low_memory=False)

# Filter the relevant columns
filtered_data = data[["season", "Over Number", "Total Runs"]]

# Filter for dot balls (Total Runs == 0)
dot_balls_data = filtered_data[filtered_data["Total Runs"] == 0]

# Group by season and count the number of balls and dot balls
season_dot_balls = dot_balls_data.groupby("season").agg({'Over Number': 'count'}).reset_index()
season_dot_balls.rename(columns={'Over Number': 'Dot Balls'}, inplace=True)

# Group by season and count the total number of balls bowled
season_total_balls = filtered_data.groupby("season").agg({'Over Number': 'size'}).reset_index()
season_total_balls.rename(columns={'Over Number': 'Total Balls'}, inplace=True)

season_dot_balls_percentage = pd.merge(season_dot_balls, season_total_balls, on='season')
season_dot_balls_percentage['Dot Balls Percentage'] = (season_dot_balls_percentage['Dot Balls'] / season_dot_balls_percentage['Total Balls']) * 100

# Plot dot balls percentage per season
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
    # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.plot(season_dot_balls_percentage["season"], season_dot_balls_percentage["Dot Balls Percentage"], marker='o', color='blue')
plt.title("Dot Balls Percentage per Season")
plt.xlabel("Season")
plt.ylabel("Dot Balls Percentage")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()