import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PSL.csv")

# Step 1: Extract "Wickets" and "season" columns
wickets_season = df[['Wickets', 'season']]

# Step 2: Group the data by season
grouped_data = wickets_season.groupby('season')

# Step 3: Define class intervals for the histogram
class_intervals = [(0, 2), (3, 4), (5, 7), (8, 10)]  # Modify as needed

# Step 4: Calculate the frequency of matches with wickets in each interval for each season
frequency_data = {}
for season, group in grouped_data:
    # Initialize frequency counts for each class interval
    freq_counts = [0] * len(class_intervals)
    
    # Count the number of matches falling within each class interval
    for idx, interval in enumerate(class_intervals):
        lower_bound, upper_bound = interval
        freq_counts[idx] = group['Wickets'].between(lower_bound, upper_bound).sum()
    
    frequency_data[season] = freq_counts

# Step 5: Plot the histogram
plt.figure(figsize=(10, 6))

# Prepare x-axis labels
x_labels = [f"{interval[0]}-{interval[1]}" for interval in class_intervals]
x_positions = range(len(x_labels))

# Plot each season's histogram as bars
for idx, (season, freq_counts) in enumerate(frequency_data.items()):
    plt.bar([pos + idx * 0.1 for pos in x_positions], freq_counts, width=0.1, align='center', label=season)
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.xlabel('Wickets per Match')
plt.ylabel('Frequency')
plt.title('Wickets per Season Histogram')
plt.xticks([pos + (len(frequency_data) - 1) * 0.05 for pos in x_positions], x_labels)
plt.legend(title='Season')
plt.grid(True)
plt.show()
