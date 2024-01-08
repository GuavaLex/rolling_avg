import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data.csv' is the name of your CSV file
# Skip the first row (header) and use semicolon as the delimiter when reading the CSV file
df = pd.read_csv('data.csv', sep=';', skiprows=1, header=None, names=['Timestamp', 'Value'])

# Convert the 'Timestamp' column to datetime format with the specified format
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%Y-%m-%d %H:%M:%S')

# Set the 'Timestamp' column as the index
df.set_index('Timestamp', inplace=True)

# Calculate the 3-minute rolling average for the 'Value' column
df['Rolling_Avg_3M'] = df['Value'].rolling(window='3T').mean()

# Example Old Value
old_value = 7741.935

# Example New Value
new_value = 7182.609

# Calculate percentage change
percentage_change = ((new_value - old_value) / old_value) * 100

# Format percentage_change to include a decimal point after three digits
formatted_percentage_change = f'{percentage_change:.3f}'

# Print intermediate values
print(f'Old Value: {old_value}')
print(f'New Value: {new_value}')
print(f'Percentage Change: {formatted_percentage_change}')

# Plot the original values and the rolling average as lines
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], label='Original Values', marker='o')
plt.plot(df.index, df['Rolling_Avg_3M'], label='3-Minute Rolling Average', color='red', linestyle='-', linewidth=2)

# Customize the plot
plt.title('3-Minute Rolling Average Line Graph')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.grid(True)

# Display min, max, avg, and numeric percentage change above the nav bar in one horizontal line
min_value = df['Value'].min()
max_value = df['Value'].max()
avg_value = df['Value'].mean()

annotation_text = f'Min: {min_value:.2f}  |  Max: {max_value:.2f}  |  Avg: {avg_value:.2f}  |  Change: {formatted_percentage_change}'

# Print final annotation
print(annotation_text)

plt.annotate(annotation_text, xy=(0.5, 1.1), xycoords="axes fraction",
             ha="center", va="center", bbox=dict(boxstyle="round", alpha=0.1),
             fontsize=10)

plt.show()
