import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Unemployment in India.csv')

# Check column names
print(data.columns)

# Rename ' Date' to 'Date' if necessary, or reference it with spaces
data.rename(columns={' Date': 'Date'}, inplace=True)

# Drop or fill missing values
data.fillna(method='ffill', inplace=True)

# Convert date with day-first parsing
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Plot unemployment rate over time using the exact column name
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data[' Estimated Unemployment Rate (%)'], color='blue', label='Unemployment Rate')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.show()

# Highlight a specific date, e.g., March 2020
plt.axvline(pd.Timestamp('2020-03-01'), color='red', linestyle='--', label='COVID-19 Spike')

# Additional analysis
peak_date = data['Date'][data[' Estimated Unemployment Rate (%)'].idxmax()]
peak_rate = data[' Estimated Unemployment Rate (%)'].max()

data['Year'] = data['Date'].dt.year
yearly_avg = data.groupby('Year')[' Estimated Unemployment Rate (%)'].mean()
yearly_avg.plot(kind='bar', figsize=(10, 5), title='Yearly Average Unemployment Rate')
plt.ylabel('Unemployment Rate (%)')
plt.show()

# Calculate yearly average unemployment rate
yearly_avg = data.groupby('Year')[' Estimated Unemployment Rate (%)'].mean()

# Display the yearly averages
print("Yearly Average Unemployment Rates:")
print(yearly_avg)


print(f'Highest unemployment rate: {peak_rate}% on {peak_date}')
print(data.head())  # Preview the first few rows
print(data.isnull().sum())  # Shows count of missing values per column

