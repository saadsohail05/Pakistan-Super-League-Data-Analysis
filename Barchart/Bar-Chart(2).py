# 2.	Top 5 Bowlers per season.
import matplotlib.pyplot as plt
import pandas as pd

def plot_top_bowlers_by_season(season):
    data = pd.read_csv('PSL.csv')

    season_data = data[data['season'] == season]

    bowler_totals = season_data.groupby('Bowler')['Wickets'].sum()

    top_5_bowlers = bowler_totals.sort_values(ascending=False).head(5)

    X = top_5_bowlers.index.tolist()
    Y = top_5_bowlers.values.tolist()
    plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+{}+{}".format(320, 130))

    plt.bar(X, Y, color='b')
    plt.title(f"Top 5 Bowlers in PSL Season {season}")
    plt.xlabel("Bowler")
    plt.ylabel("Total Wickets")

    plt.xticks(rotation=10)

    plt.show()

# Take input for the season
season_input = "2016/17"# you can tak input of every season

# Plot the top five bowlers for the specified season
plot_top_bowlers_by_season(season_input)
