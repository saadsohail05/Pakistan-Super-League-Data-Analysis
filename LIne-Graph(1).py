import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("PSL.csv", low_memory=False)

# Filter the relevant columns
filtered_data = data[["season", "Batter runs", "event match_number"]]

# Filter for fours (4) and sixes (6) only
filtered_data = filtered_data[filtered_data["Batter runs"].isin([4, 6])]

# Group by season and calculate total fours and sixes
season_data = filtered_data.groupby("season").size().reset_index(name='Total Boundaries')

# Calculate the total number of matches per season
matches_per_season = filtered_data.groupby("season")["event match_number"].nunique().reset_index(name='Total Matches')

# Merge total boundaries and total matches dataframes
season_data = pd.merge(season_data, matches_per_season, on="season")

# Calculate average boundaries per match per season
season_data["Average Boundaries per Match"] = season_data["Total Boundaries"] / season_data["Total Matches"]

# Plot average boundaries per match per season
plt.figure(figsize=(10, 5))
plt.plot(season_data["season"], season_data["Average Boundaries per Match"], marker='o', color='green')
plt.title("Average Boundaries per Match per Season")
plt.xlabel("Season")
plt.ylabel("Average Boundaries per Match")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()