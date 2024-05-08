import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("PSL.csv")

# Extract columns related to extras
extras_columns = ['Byes', 'Legbyes', 'Noballs', 'Penalty', 'Wides']
extras_data = df[extras_columns]

# Calculate frequency of each type of extra
extras_frequency = extras_data.sum()

# Plotting the frequency polygon
plt.figure(figsize=(10, 6))
plt.plot(extras_frequency.index, extras_frequency.values, marker='o', linestyle='-')
plt.title('Frequency Polygon of Extras in PSL')
plt.xlabel('Type of Extra')
plt.ylabel('Frequency')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
