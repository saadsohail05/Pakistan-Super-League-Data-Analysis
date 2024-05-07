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

# Store the results without table
print("Average Target per Season of Every Team:")
for season in average_target_stats_per_season['season'].unique():
    print(f"Season {season}:")
    season_data = average_target_stats_per_season[average_target_stats_per_season['season'] == season]
    for index, row in season_data.iterrows():
        team = row['Team']
        mean_target = row['Target Runs_mean']
        median_target = row['Target Runs_median']
        mode_target = row['Target Runs']
        print(f"  Team: {team}")
        print(f"    Mean Target: {mean_target}")
        print(f"    Median Target: {median_target}")
        print(f"    Mode Target: {mode_target}")
