import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Aggregate data by date and venue
psl_data_agg = psl_data.groupby(['dates', 'venue']).agg({
    'Total Runs': 'sum',
    'Wickets': 'sum',
    'runs.extras': 'sum'
}).reset_index()

# Create box plot for runs scored across different venues
plt.figure(figsize=(15, 6))  # Increase the figure size
ax = psl_data_agg.boxplot(column='Total Runs', by='venue', figsize=(15,6), rot=0)
plt.title('Distribution of Runs Scored Across Different Venues', fontsize=16)  # Increase title font size
plt.xlabel('Venue', fontsize=14)  # Increase x-axis label font size
plt.ylabel('Runs Scored', fontsize=14)  # Increase y-axis label font size
plt.xticks(fontsize=5)  # Increase x-axis tick label font size
plt.show()

# Create box plot for wickets taken across different venues
plt.figure(figsize=(15, 6))  # Increase the figure size
ax = psl_data_agg.boxplot(column='Wickets', by='venue', figsize=(15,6), rot=0)
plt.title('Distribution of Wickets Taken Across Different Venues', fontsize=16)  # Increase title font size
plt.xlabel('Venue', fontsize=14)  # Increase x-axis label font size
plt.ylabel('Wickets Taken', fontsize=14)  # Increase y-axis label font size
plt.xticks(fontsize=5)  # Increase x-axis tick label font size
plt.show()

# Create box plot for extras conceded across different venues
plt.figure(figsize=(15, 6))  # Increase the figure size
ax = psl_data_agg.boxplot(column='runs.extras', by='venue', figsize=(15,6), rot=0)
plt.title('Distribution of Extras Conceded Across Different Venues', fontsize=16)  # Increase title font size
plt.xlabel('Venue', fontsize=14)  # Increase x-axis label font size
plt.ylabel('Extras Conceded', fontsize=14)  # Increase y-axis label font size
plt.xticks(fontsize=5)  # Increase x-axis tick label font size
plt.show()
