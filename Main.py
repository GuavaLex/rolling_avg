import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data_1.csv' is the name of your CSV file
# Skip the first row (header) and use semicolon as the delimiter when reading the CSV file
df = pd.read_csv('data_1.csv', sep=';', skiprows=1, header=None, names=['Timestamp', 'Value'])

# Convert the 'Timestamp' column to datetime format with the specified format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Set the 'Timestamp' column as the index
df.set_index('Timestamp', inplace=True)

# Filter data for timestamps between 7:29 am and 2:23 pm
df_filtered = df[(df.index.time >= pd.to_datetime('07:29:00').time()) & (df.index.time <= pd.to_datetime('14:23:00').time())]

# Calculate the 3-minute rolling average for the 'Value' column
df_filtered['Rolling_Avg_3M'] = df_filtered['Value'].rolling(window='3T').mean()

# Plot the original values and the rolling average as lines
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Original Values', marker='o', linestyle='', markersize=4, alpha=0.5)
plt.plot(df_filtered.index, df_filtered['Rolling_Avg_3M'], label='3-Minute Rolling Average', color='red', linestyle='-', linewidth=2)

# Customize the plot
plt.title('3-Minute Rolling Average Line Graph from 7:29 am to 2:23 pm')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Calculate min, max, avg, and percentage change within the time period
min_value = df_filtered['Value'].min()
max_value = df_filtered['Value'].max()
avg_value = df_filtered['Value'].mean()
percentage_change = ((df_filtered['Value'].iloc[-1] - df_filtered['Value'].iloc[0]) / df_filtered['Value'].iloc[0]) * 100

# Format percentage_change to include a decimal point after three digits
formatted_percentage_change = f'{percentage_change:.3f}'

annotation_text = f'Min: {min_value:.2f}  |  Max: {max_value:.2f}  |  Avg: {avg_value:.2f}  |  Change: {formatted_percentage_change}'

plt.annotate(annotation_text, xy=(0.5, 1.1), xycoords="axes fraction",
             ha="center", va="center", bbox=dict(boxstyle="round", alpha=0.1),
             fontsize=10)

plt.show()
