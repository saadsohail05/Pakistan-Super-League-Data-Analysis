import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('PSL.csv')

# Prepare the data
X = df['Wickets']  # Independent variable: Wickets lost
Y = df['Total Runs']  # Dependent variable: Total runs scored

# Calculate the mean of X and Y
mean_X = X.mean()
mean_Y = Y.mean()

# Calculate the covariance of X and Y
covariance_XY = sum((X - mean_X) * (Y - mean_Y))

# Calculate the variance of X
variance_X = sum((X - mean_X) ** 2)

# Calculate the slope and intercept
slope = covariance_XY / variance_X
intercept = mean_Y - slope * mean_X
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
# Plotting the actual data points
plt.scatter(X, Y, color='blue', alpha=0.7, edgecolors="k", label='Data Points')

# Calculate and plot the regression line
Y_predicted = [slope * x + intercept for x in X]
plt.plot(X, Y_predicted, color='red', linewidth=2.5, label='Regression Line')

# Customizing the plot
plt.title('Total Runs vs Wickets (Ball-by-Ball Data)', fontsize=16)
plt.xlabel('Wickets Lost', fontsize=14)
plt.ylabel('Total Runs Scored', fontsize=14)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)

# Show the plot
plt.show()

# Print regression parameters
print("Slope:", slope)
print("Intercept:", intercept)
