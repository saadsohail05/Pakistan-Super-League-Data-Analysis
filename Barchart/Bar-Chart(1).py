#1.	Top 5 Batters per season.
import matplotlib.pyplot as plt
import pandas as pd

def plot_top_5_batters(season):
    # Read the data from CSV
    data = pd.read_csv('PSL.csv')
    
    season_data = data[data['season'] == season]
    
    batter_totals = season_data.groupby('Batter')['Batter runs'].sum()
    
    top_5_batters = batter_totals.sort_values(ascending=False).head(5)
    
    X = top_5_batters.index.tolist()
    Y = top_5_batters.values.tolist()
    
    plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+{}+{}".format(128, 22))
   

    plt.bar(X, Y, color='g')
    plt.title("Top 5 Batters in Season {}".format(season))
    plt.xlabel("Batter")
    plt.ylabel("Total Runs")
    
    plt.xticks(rotation=12)
  
    plt.show()

# Take input for the season
season = "2018/19" # you can change seasons here
plot_top_5_batters(season)
