import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Calculating run rate
psl_data['Run Rate'] = psl_data['Total Runs'] / psl_data['Overs']

# Calculating variance of run rate per season
variance_run_rate_per_season = psl_data.groupby('season')['Run Rate'].var().reset_index()

# Store the results without table
print("Variance of Run Rate per Season:")
for index, row in variance_run_rate_per_season.iterrows():
    season = row['season']
    variance = row['Run Rate']
    print(f"Season {season}:")
    print(f"  Variance of Run Rate: {variance}")
