import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv("PSL.csv")

# Count the number of tosses won by each team
toss_winner_counts = df['Toss Winner'].value_counts()

# Get the teams that won the most tosses
most_toss_winner = toss_winner_counts.idxmax()

# Plotting a pie chart for teams with most toss wins
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(320, 130))
plt.pie(toss_winner_counts, labels=toss_winner_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Teams with Most Toss Wins', fontsize=16, fontweight='bold', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()  # Adjust layout to prevent labels from being cut off
plt.show()

print(f"The team with the most toss wins: {most_toss_winner} ({toss_winner_counts[most_toss_winner]} wins)")
