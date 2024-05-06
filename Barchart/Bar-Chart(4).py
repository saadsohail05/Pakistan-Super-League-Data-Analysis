#4.	Boundaries of death over and powerplay (component bar-chart)

import matplotlib.pyplot as plt
import pandas as pd

# Read the data from CSV file
data = pd.read_csv('PSL.csv')

# Filter data to include only rows where Total Runs represent boundaries (4 or 6)
boundary_data = data[data['Total Runs'].isin([4, 6])]

# Filter data to include only boundaries in overs 1-6 and 16-20
boundary_data = boundary_data[(boundary_data['Over Number'].isin(range(1, 7))) | (boundary_data['Over Number'].isin(range(16, 21)))]

# Group data by season and over number range, and count the number of boundaries for each group
season_over_boundary_counts = boundary_data.groupby(['season', pd.cut(boundary_data['Over Number'], bins=[0, 6, 20], labels=['Powerplay', 'Death Over'])]).size().unstack(fill_value=0)


# Plot the component bar chart
season_over_boundary_counts.plot(kind='bar', stacked=True)
plt.title("Total Boundaries (Fours and Sixes) in Powerplay and Death Overs Per Season")
plt.xlabel("Season")
plt.ylabel("Total Boundaries")
plt.xticks(rotation=45)

# Show the plot

plt.legend(title='Over Range')
plt.tight_layout()
plt.show()
