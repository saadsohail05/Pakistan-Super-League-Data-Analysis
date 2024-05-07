import pandas as pd

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Calculating run rate
psl_data['Run Rate'] = psl_data['Total Runs'] / psl_data['Overs']

# Calculating standard deviation of run rate per season
std_dev_run_rate_per_season = psl_data.groupby('season')['Run Rate'].std().reset_index()

# Store the results without table
print("Standard Deviation of Run Rate per Season:")
for index, row in std_dev_run_rate_per_season.iterrows():
    season = row['season']
    std_dev = row['Run Rate']
    print(f"Season {season}:")
    print(f"  Standard Deviation of Run Rate: {std_dev}")
