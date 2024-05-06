import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("PSL.csv")

# Count the number of matches held at each venue
venue_counts = df['venue'].value_counts()

# Get the venue with the maximum number of matches
max_venue = venue_counts.idxmax()

# Define colors for the pie chart
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

# Plotting a pie chart without labels
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(320, 130))
patches, texts, autotexts = plt.pie(venue_counts, labels=None, autopct='%1.1f%%', startangle=140, colors=colors, textprops={'fontsize': 12})
plt.title('Distribution of Matches Held at Different Venues', fontsize=18, fontweight='bold', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Create legend with custom labels and colors
plt.legend(patches, venue_counts.index, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)

plt.tight_layout()  # Adjust layout to prevent labels from being cut off
plt.show()

print(f"The venue with the most matches: {max_venue} ({venue_counts[max_venue]} matches)")
