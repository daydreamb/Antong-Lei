import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"

# 1)Filter the data to include only weekdays (Monday to Friday) and plot a line graph showing the pedestrian counts for each day of the week.

data = pd.read_csv(url)
data['Date'] = pd.to_datetime(data['Date'])
data['Day_of_Week'] = data['Date'].dt.day_name()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekday_data = data[data['Day_of_Week'].isin(weekdays)]
daily_counts = weekday_data.groupby('Day_of_Week')['Brooklyn Bridge'].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x=daily_counts.index, y=daily_counts.values, marker='o')
plt.title('Average Pedestrian Counts on Brooklyn Bridge (Weekdays)')
plt.xlabel('Day of the Week')
plt.ylabel('Pedestrian Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian activity
data['Year'] = data['Date'].dt.year
bridge_data_2019 = data[(data['Year'] == 2019) & (data['Location'] == 'Brooklyn Bridge')]

weather_correlation = bridge_data_2019[['Brooklyn Bridge', 'Summary']].groupby('Summary').mean()

plt.figure(figsize=(10, 6))
sns.heatmap(weather_correlation, annot=True, cmap='coolwarm')
plt.title('Correlation between Weather Conditions and Pedestrian Counts (2019)')
plt.xlabel('Weather Summary')
plt.ylabel('Pedestrian Count')
plt.tight_layout()
plt.show()

# Implement a custom function to categorize time of day into morning, afternoon, evening, and night, and create a new column in the DataFrame to store these categories. Use this new column to analyze pedestrian activity patterns throughout the day.
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

data['Time_of_Day'] = data['Date'].dt.hour.apply(categorize_time_of_day)
time_of_day_counts = data.groupby('Time_of_Day')['Brooklyn Bridge'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(x=time_of_day_counts.index, y=time_of_day_counts.values, palette='muted')
plt.title('Average Pedestrian Counts on Brooklyn Bridge by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Average Pedestrian Count')
plt.tight_layout()
plt.show()
