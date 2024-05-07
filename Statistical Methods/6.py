import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
psl_data = pd.read_csv("PSL.csv")

# Create box plot for runs scored across different seasons
plt.figure(figsize=(10, 6))
psl_data.boxplot(column='Total Runs', by='season', figsize=(10,6))
plt.title('Distribution of Runs Scored Across Different Seasons')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.show()

# Create box plot for wickets taken across different seasons
plt.figure(figsize=(10, 6))
psl_data.boxplot(column='Wickets', by='season', figsize=(10,6))
plt.title('Distribution of Wickets Taken Across Different Seasons')
plt.xlabel('Season')
plt.ylabel('Wickets Taken')
plt.show()

# Create box plot for extras conceded across different seasons
plt.figure(figsize=(10, 6))
psl_data.boxplot(column='runs.extras', by='season', figsize=(10,6))
plt.title('Distribution of Extras Conceded Across Different Seasons')
plt.xlabel('Season')
plt.ylabel('Extras Conceded')
plt.show()

# Create box plot for runs scored across different venues
plt.figure(figsize=(15, 6))
psl_data.boxplot(column='Total Runs', by='venue', figsize=(15,6), rot=90)
plt.title('Distribution of Runs Scored Across Different Venues')
plt.xlabel('Venue')
plt.ylabel('Runs Scored')
plt.show()

# Create box plot for wickets taken across different venues
plt.figure(figsize=(15, 6))
psl_data.boxplot(column='Wickets', by='venue', figsize=(15,6), rot=90)
plt.title('Distribution of Wickets Taken Across Different Venues')
plt.xlabel('Venue')
plt.ylabel('Wickets Taken')
plt.show()

# Create box plot for extras conceded across different venues
plt.figure(figsize=(15, 6))
psl_data.boxplot(column='runs.extras', by='venue', figsize=(15,6), rot=90)
plt.title('Distribution of Extras Conceded Across Different Venues')
plt.xlabel('Venue')
plt.ylabel('Extras Conceded')
plt.show()
