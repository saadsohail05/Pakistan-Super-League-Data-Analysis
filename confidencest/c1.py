import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

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

# Calculate the residuals
residuals = Y - (slope * X + intercept)

# Calculate the standard deviation of the residuals
std_residuals = np.std(residuals, ddof=2)  # ddof=2 for unbiased estimation

# Calculate the standard error of the slope
std_error_slope = std_residuals / np.sqrt(variance_X)

# Calculate the critical value for 95% confidence interval
degrees_of_freedom = len(X) - 2  # degrees of freedom = n - p - 1 (p is the number of parameters)
t_critical = t.ppf(0.975, df=degrees_of_freedom)  # 2-tailed t-test, alpha=0.05

# Calculate the confidence interval for the slope
slope_lower_bound = slope - t_critical * std_error_slope
slope_upper_bound = slope + t_critical * std_error_slope

# Calculate the standard error of the intercept
std_error_intercept = std_residuals * np.sqrt(1 / len(X) + (mean_X ** 2) / variance_X)

# Calculate the confidence interval for the intercept
intercept_lower_bound = intercept - t_critical * std_error_intercept
intercept_upper_bound = intercept + t_critical * std_error_intercept

# Plotting the regression line with confidence intervals
plt.figure(figsize=(12, 7))
plt.scatter(X, Y, color='blue', alpha=0.7, edgecolors="k", label='Data Points')
plt.plot(X, slope * X + intercept, color='red', linewidth=2.5, label='Regression Line')
plt.fill_between(X, (slope_lower_bound * X + intercept_lower_bound), (slope_upper_bound * X + intercept_upper_bound), color='gray', alpha=0.2, label='95% Confidence Interval')
plt.title('Total Runs vs Wickets (Ball-by-Ball Data)', fontsize=16)
plt.xlabel('Wickets Lost', fontsize=14)
plt.ylabel('Total Runs Scored', fontsize=14)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)
plt.show()

# Print regression parameters and confidence intervals
print("Slope:", slope)
print("Intercept:", intercept)
print("95% Confidence Interval for Slope:", (slope_lower_bound, slope_upper_bound))
print("95% Confidence Interval for Intercept:", (intercept_lower_bound, intercept_upper_bound))
