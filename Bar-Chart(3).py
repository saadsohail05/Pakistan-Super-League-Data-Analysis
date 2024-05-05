# 3.	Boundaries per season.
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from CSV file
data = pd.read_csv('PSL.csv')

# Filter data to include only rows where Total Runs is 4 or 6 (boundaries)
boundary_data = data[data['Total Runs'].isin([4, 6])]

# Group data by season and count the number of boundaries for each season
season_boundary_counts = boundary_data.groupby('season').size().reset_index(name='Boundary Count')

# Extract X and Y values
X = season_boundary_counts['season']
Y = season_boundary_counts['Boundary Count']

# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Total Boundaries (Fours and Sixes) Per Season")
plt.xlabel("Season")
plt.ylabel("Total Boundaries")
plt.xticks(rotation=15)

# Show the plot
plt.show()
