import csv
from collections import defaultdict

# Load the data from the CSV file
data = []
with open('PSL.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        batter = row[4]
        batter_runs = float(row[7])
        ball_number = float(row[3])
        data.append((batter, batter_runs, ball_number))

# Group the data by batter
batter_data = defaultdict(list)
for batter, batter_runs, ball_number in data:
    batter_data[batter].append((batter_runs, ball_number))

# Create feature and target variables
X = []
y = []
for batter, runs_balls in batter_data.items():
    total_runs = sum(run for run, _ in runs_balls)
    total_balls = sum(1 for _, _ in runs_balls)
    X.append(total_balls)
    y.append(total_runs)

# Create a linear regression model
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array(X).reshape(-1, 1)
y = np.array(y)

model = LinearRegression()
model.fit(X, y)

# Get the coefficients, intercept, and R-squared
coef = model.coef_[0]
intercept = model.intercept_
r_squared = model.score(X, y)

# Print the results
print(f'Coefficient: {coef}')
print(f'Intercept: {intercept}')
print(f'R-squared: {r_squared}')

# Visualize the results
import matplotlib.pyplot as plt
plt.figure(figsize=(12.8, 7.2))  # 1280x720 pixels
      # Center the plot window on the screen
manager = plt.get_current_fig_manager()
manager.window.wm_geometry("+{}+{}".format(128, 22))
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=2)
plt.xlabel('Number of Balls Faced')
plt.ylabel('Total Runs Scored')
plt.title('Linear Regression: Total Runs vs Balls Faced')
plt.show()