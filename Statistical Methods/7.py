import pandas as pd
from scipy.stats import chi2_contingency

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Create a contingency table for match outcome vs venue
contingency_table = pd.crosstab(psl_data['Winner'], psl_data['venue'])

# Perform Chi-square test for independence
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Print the results
print("Chi-square Test for Independence (Match Outcome vs Venue):")
print(f"Chi-square value: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
