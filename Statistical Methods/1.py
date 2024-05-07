import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Extracting the over number
psl_data['Over'] = psl_data['Over Number'] + 1

# Creating a new column to categorize overs
psl_data['Over_Category'] = pd.cut(psl_data['Over'], bins=[0, 6, 15, 20], labels=['Powerplay', 'Middle Overs', 'Death Overs'])

# Calculating total runs scored in each over category per season
runs_per_season_over_category = psl_data.groupby(['season', 'Over_Category'])['Total Runs'].sum().reset_index()

# Calculating total matches per season
matches_per_season = psl_data.groupby('season')['event match_number'].nunique().reset_index()

# Merging total runs and total matches per season
average_runs_per_season_over_category = pd.merge(runs_per_season_over_category, matches_per_season, on='season')

# Calculating average runs per over category per season
average_runs_per_season_over_category['Average Runs'] = average_runs_per_season_over_category['Total Runs'] / average_runs_per_season_over_category['event match_number']

# Pivoting the table to get the desired format
average_runs_per_season_over_category_pivot = average_runs_per_season_over_category.pivot_table(index='season', columns='Over_Category', values='Average Runs')

# Store the results without table
print("Average Score of Teams in Powerplay, Middle Overs, and Death Overs per Season:")
for season in average_runs_per_season_over_category_pivot.index:
    powerplay_avg = average_runs_per_season_over_category_pivot.loc[season, 'Powerplay']
    middle_overs_avg = average_runs_per_season_over_category_pivot.loc[season, 'Middle Overs']
    death_overs_avg = average_runs_per_season_over_category_pivot.loc[season, 'Death Overs']
    print(f"Season {season}:")
    print(f"  Powerplay Average: {powerplay_avg}")
    print(f"  Middle Overs Average: {middle_overs_avg}")
    print(f"  Death Overs Average: {death_overs_avg}")
