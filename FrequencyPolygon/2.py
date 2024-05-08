import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('PSL.csv')

# Filter the data for 'struckdown' and 'upheld' review decisions
review_decision_data = data[data['Review Decision'].isin(['struck down', 'upheld'])]['Review Decision']

# Calculate frequency of 'struckdown' and 'upheld' review decisions
review_decision_frequency = review_decision_data.value_counts()

# Plotting the frequency polygon
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.plot(review_decision_frequency.index, review_decision_frequency.values, marker='o', linestyle='-')
plt.title('Frequency Polygon of Review Decisions (Struckdown vs. Upheld) in PSL')
plt.xlabel('Review Decision Type')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
