import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PSL.csv")

# Extract columns related to extras
extras_columns = ['Byes', 'Legbyes', 'Noballs', 'Penalty', 'Wides']
extras_data = df[extras_columns]

# Calculate frequency of each type of extra
extras_frequency = extras_data.sum()

# Plotting the frequency polygon
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.plot(extras_frequency.index, extras_frequency.values, marker='o', linestyle='-')
plt.title('Frequency Polygon of Extras in PSL')
plt.xlabel('Type of Extra')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
