import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PSL.csv')

# Exclude rows where Wicket Type is 0
dismissal_type_data = data[data['Wicket Type'] != '0']['Wicket Type']

# Calculate frequency of each dismissal type
dismissal_type_frequency = dismissal_type_data.value_counts()

# Plotting the frequency polygon
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.plot(dismissal_type_frequency.index, dismissal_type_frequency.values, marker='o', linestyle='-')
plt.title('Frequency Polygon of Dismissal Types in PSL')
plt.xlabel('Dismissal Type')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
