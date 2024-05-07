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

# Store the results without table
print("Average Wickets of Teams in Powerplay, Middle Overs, and Death Overs per Season:")
for season in average_wickets_per_season_over_category_pivot.index:
    powerplay_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Powerplay']
    middle_overs_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Middle Overs']
    death_overs_avg = average_wickets_per_season_over_category_pivot.loc[season, 'Death Overs']
    print(f"Season {season}:")
    print(f"  Powerplay Average Wickets: {powerplay_avg}")
    print(f"  Middle Overs Average Wickets: {middle_overs_avg}")
    print(f"  Death Overs Average Wickets: {death_overs_avg}")
