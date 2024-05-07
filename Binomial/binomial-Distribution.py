import pandas as pd

import numpy as np  
import matplotlib.pyplot as plt  
from scipy.stats import binom  
# Read the CSV file into a DataFrame
df = pd.read_csv("PSL.csv")

# Initialize variables to store the previous winner and toss winner
prev_winner = None
prev_toss_winner = None
prev_eventmatchnumber=None

same_toss_and_winner_count = 0
match_count=0

for index, row in df.iterrows():
    current_winner = row['Winner']
    current_toss_winner = row['Toss Winner']
    
    if (current_winner != prev_winner or current_toss_winner != prev_toss_winner) and current_winner == current_toss_winner :
        # Increment the count
        same_toss_and_winner_count += 1
    
    prev_winner = current_winner
    prev_toss_winner = current_toss_winner


for index, row in df.iterrows():
    current_eventmatchnumber = row['Winner']
    
    if current_eventmatchnumber != prev_eventmatchnumber  :
        match_count += 1
    
    prev_eventmatchnumber = current_eventmatchnumber
match_count=440
n = match_count  # Number of coin flips  
p = same_toss_and_winner_count/match_count  # Probability of heads (success)  
k_values = np.arange(0, n + 1)  
pmf = binom.pmf(k_values, n, p)  
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.bar(k_values, pmf)  
plt.xlabel('Number of Match Win when Toss win')  
plt.ylabel('Probability')  
plt.title('Binomial Distribution')  
plt.show()  