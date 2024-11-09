# Unemployment Analysis with Python 

## Project Objectives
This project analyzes unemployment rates over time, with a specific focus on trends and spikes in unemployment in India. The main goal is to visualize unemployment trends and calculate yearly averages to understand how certain events, such as COVID-19, have impacted unemployment rates.

## Data Source
The dataset used for this analysis is the **Unemployment in India** dataset, which provides monthly unemployment rates across different regions and demographics in India. The data includes fields for unemployment rate, employment estimates, and labor participation rate.

## Analysis Approach
1. **Data Cleaning**: Missing values were handled by using forward fill to ensure continuity in data.
2. **Time Series Visualization**: The unemployment rate over time was plotted to identify trends and potential anomalies, with special markers for key events (e.g., COVID-19 in March 2020).
3. **Yearly Analysis**: Calculated yearly averages for unemployment rates to compare yearly trends and provide a clearer picture of economic impact.

## Results
- **Average Unemployment Rates by Year**:
  - **2019**: 9.40%
  - **2020**: 14.46%
- The highest unemployment rate observed was approximately **76.74%** in April 2020.
- Visualizations highlight the spike in unemployment during the COVID-19 pandemic and allow for comparisons between years.

## Instructions to Run
1. Ensure `pandas` and `matplotlib` are installed.
2. Run the Python script `unemployment_analysis.py` to load data, visualize trends, and display calculated yearly averages.
