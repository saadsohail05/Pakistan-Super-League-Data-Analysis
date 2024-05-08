import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PSL.csv')

# Group the data by over number and calculate the frequency of runs made in each over
runs_per_over = data.groupby('Over Number')['Total Runs'].value_counts().unstack().fillna(0)

# Calculate the total frequency of runs made in each over
total_runs_per_over = runs_per_over.sum(axis=1)

# Plotting the frequency polygon
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.plot(total_runs_per_over.index, total_runs_per_over.values, marker='o', linestyle='-')
plt.title('Frequency Polygon of Runs Made in Every Over in PSL')
plt.xlabel('Over Number')
plt.ylabel('Frequency of Runs Made')
plt.grid(True)
plt.xticks(range(1, 21))
plt.tight_layout()
plt.show()
