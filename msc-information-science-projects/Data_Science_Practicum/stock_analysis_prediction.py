#Hiba Abidelkarem

import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler

# Load files
stocks_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_stocks.csv')
index_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_index.csv')
companies_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_companies.csv')

# Convert 'Date' columns to datetime
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'], format='%Y-%m-%d', errors='coerce')
index_df['Date'] = pd.to_datetime(index_df['Date'], format='%Y-%m-%d', errors='coerce')

# Clean column names
stocks_df.columns = stocks_df.columns.str.strip().str.lower().str.replace(' ', '_')
index_df.columns = index_df.columns.str.strip().str.lower().str.replace(' ', '_')
companies_df.columns = companies_df.columns.str.strip().str.lower().str.replace(' ', '_')

# Ensure 'date' column is consistently named 'Date'
stocks_df.rename(columns={'date': 'Date'}, inplace=True)
index_df.rename(columns={'date': 'Date'}, inplace=True)

# Print missing values before cleaning
print("Missing values before cleaning:")
print("Stocks DataFrame:")
print(stocks_df.isnull().sum())
print("\nIndex DataFrame:")
print(index_df.isnull().sum())
print("\nCompanies DataFrame:")
print(companies_df.isnull().sum())

# Handle missing values
# For stocks_df, use forward fill
stocks_df.fillna(method='ffill', inplace=True)

# For companies_df, fill categorical missing values with 'Unknown'
companies_df['state'].fillna('Unknown', inplace=True)
companies_df['ebitda'].fillna(companies_df['ebitda'].median(), inplace=True)
companies_df['revenuegrowth'].fillna(companies_df['revenuegrowth'].median(), inplace=True)
companies_df['fulltimeemployees'].fillna(companies_df['fulltimeemployees'].median(), inplace=True)

#  KNN Imputer for more sophisticated imputation
# Prepare data for KNN Imputation (excluding 'symbol' which is categorical)
numeric_cols_companies = ['ebitda', 'revenuegrowth', 'fulltimeemployees']
knn_imputer = KNNImputer(n_neighbors=5)
companies_df[numeric_cols_companies] = knn_imputer.fit_transform(companies_df[numeric_cols_companies])

# Print missing values after cleaning
print("\nMissing values after cleaning:")
print("Stocks DataFrame:")
print(stocks_df.isnull().sum())
print("\nIndex DataFrame:")
print(index_df.isnull().sum())
print("\nCompanies DataFrame:")
print(companies_df.isnull().sum())

# Merge stocks_df and index_df on 'Date'
merged_df = pd.merge(stocks_df, index_df, on='Date', how='inner')

# Merge with companies_df on 'symbol'
final_merged_df = pd.merge(merged_df, companies_df, on='symbol', how='left')

# Normalize numerical columns (e.g., stock prices)
numerical_cols = ['open', 'high', 'low', 'close', 'volume']  # Adjust if needed
scaler = MinMaxScaler()
final_merged_df[numerical_cols] = scaler.fit_transform(final_merged_df[numerical_cols])

# Save cleaned files
stocks_df.to_csv('C://Users//afnan abed alkreem//Downloads//sp500_stocks_cleaned.csv', index=False)
index_df.to_csv('C://Users//afnan abed alkreem//Downloads//sp500_index_cleaned.csv', index=False)
companies_df.to_csv('C://Users//afnan abed alkreem//Downloads//sp500_companies_cleaned.csv', index=False)
final_merged_df.to_csv('C://Users//afnan abed alkreem//Downloads//sp500_merged_cleaned.csv', index=False)

print("\nFiles have been cleaned and saved.")


#-----------------------------------------
#לתאר את הדאטה תוך שימוש בסטטיסטיקה תיאורית ודיאגרמות פשוטות. 
# סטטיסטיקה תיאורית עבור הנתונים של מניות
import matplotlib.pyplot as plt

print(stocks_df.describe())

# היסטוגרמה עבור מחירי הסגירה של מניה לדוגמה
plt.figure(figsize=(10, 6))
plt.hist(stocks_df['close'].dropna(), bins=50, edgecolor='black')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.title('Histogram of Closing Prices')
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot([stocks_df[stocks_df['symbol'] == symbol]['close'].dropna() for symbol in stocks_df['symbol'].unique()],
            labels=stocks_df['symbol'].unique())
plt.xlabel('Stock Symbol')
plt.ylabel('Closing Price')
plt.title('Box Plot of Closing Prices by Stock')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(14, 7))
import pandas as pd
import matplotlib.pyplot as plt

# Example DataFrame
example_stock = stocks_df[stocks_df['symbol'] == 'AAPL']

# Ensure 'Date' is the index and in datetime format
example_stock.set_index('Date', inplace=True)
example_stock.index = pd.to_datetime(example_stock.index)

# Plotting
plt.figure(figsize=(12, 6))
plt.scatter(example_stock.index, example_stock['close'], color='blue', s=10)

plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Scatter Plot of Closing Prices for AAPL')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# גרף קווי של מדד S&P 500
plt.plot(index_df['Date'], index_df['s&p500'], label='S&P 500', color='blue')
plt.title('S&P 500 Index Over Time')
plt.xlabel('Date')
plt.ylabel('S&P 500 Index Value')
plt.grid(True)
plt.show()

# גרף פיזור
plt.scatter(companies_df['marketcap'], companies_df['currentprice'], color='green', s=10)
plt.title('Market Cap vs Current Price')
plt.xlabel('Market Cap')
plt.ylabel('Current Price')
plt.grid(True)
plt.show()



#-----------------------------------------
#השערה 1
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the dataset
data_file_path = 'C://Users//afnan abed alkreem//Downloads//sp500_stocks_cleaned.csv'
df = pd.read_csv(data_file_path)

# Convert 'Date' column to datetime format if it isn't already
df['Date'] = pd.to_datetime(df['Date'])

# List of major companies
major_companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Initialize a figure for plotting
plt.figure(figsize=(12, 8))

# Dictionary to store statistics
company_stats = {}

# Loop through each major company
for symbol in major_companies:
    # Filter data for the company
    company_data = df[df['symbol'] == symbol].copy()
    
    # Calculate daily returns
    company_data['daily_return'] = company_data['close'].pct_change()
    
    # Drop rows with NaN values resulting from pct_change
    company_data.dropna(subset=['daily_return'], inplace=True)
    
    # Plot daily returns for the company
    plt.plot(company_data['Date'], company_data['daily_return'], label=symbol)
    
    # Calculate mean and standard deviation of daily returns
    mean_return = company_data['daily_return'].mean()
    std_return = company_data['daily_return'].std()
    
    # Store statistics in the dictionary
    company_stats[symbol] = {'mean': mean_return, 'std': std_return}

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Daily Return')
plt.title('Daily Returns of Major Companies')
plt.legend(loc='best')

plt.gca().xaxis.set_major_locator(mdates.YearLocator())  
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format to show only the year

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot with tight layout
plt.tight_layout()
plt.show()

# Print out the mean and standard deviation of daily returns for each company
print("\nMean and Standard Deviation of Daily Returns for Major Companies:")
for symbol, stats in company_stats.items():
    print(f"{symbol}: Mean = {stats['mean']:.6f}, Std Dev = {stats['std']:.6f}")

#------------------------------------------
#השערה 1 עם ימים
import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data (assuming the file has already been cleaned and processed)
stock_data = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_merged_cleaned.csv')

# Convert 'Date' to datetime format if it's not already
stock_data['Date'] = pd.to_datetime(stock_data['Date'], format='%Y-%m-%d')

# Sort by 'symbol' and 'Date' to ensure correct calculation of daily returns
stock_data = stock_data.sort_values(by=['symbol', 'Date'])

# Calculate daily returns
# Ensure 'close' column exists for daily return calculation
if 'close' in stock_data.columns:
    stock_data['daily_return'] = stock_data.groupby('symbol')['close'].pct_change()
else:
    print("The 'close' column is missing from the dataset.")

# Filter the data for the year 2024
companies_tech = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
stock_data_2024 = stock_data[stock_data['Date'].dt.year == 2024]
filtered_data_2024 = stock_data_2024[stock_data_2024['symbol'].isin(companies_tech)]

# Create a plot for the daily returns of each company in 2024
plt.figure(figsize=(12, 6))

for symbol in companies_tech:
    company_data = filtered_data_2024[filtered_data_2024['symbol'] == symbol]
    plt.plot(company_data['Date'], company_data['daily_return'], label=symbol)

# Add titles and labels
plt.title('Daily Returns for Tech Companies in 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Return (%)', fontsize=12)
plt.xticks(rotation=45)  # Rotate the x-axis dates for readability
plt.legend(loc='best')
plt.tight_layout()

# Show the plot
plt.show()

# Calculate the average daily returns and standard deviations for 2024
average_daily_returns = filtered_data_2024.groupby('symbol')['daily_return'].mean()
std_daily_returns = filtered_data_2024.groupby('symbol')['daily_return'].std()

# Print the results
print("\nAverage Daily Returns for 2024:")
print(average_daily_returns)

print("\nStandard Deviation of Daily Returns for 2024:")
print(std_daily_returns)



#------------------------------------------
#השערה 2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Ensure correct date format for 'Date' columns in both DataFrames
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'], errors='coerce')
index_df['Date'] = pd.to_datetime(index_df['Date'], errors='coerce')

# 1. Calculate daily returns for both stocks and index
stocks_df['daily_return'] = stocks_df.groupby('symbol')['close'].pct_change()
index_df['index_return'] = index_df['s&p500'].pct_change()

# Merge stock data with index data on date
merged_df = pd.merge(stocks_df, index_df[['Date', 'index_return']], on='Date', how='inner')

# Correlation analysis
merged_df.dropna(subset=['daily_return', 'index_return'], inplace=True)
correlation = merged_df['daily_return'].corr(merged_df['index_return'])
print(f"Correlation between stock returns and index returns: {correlation:.4f}")

# Linear regression
X = merged_df[['index_return']]
y = merged_df['daily_return']
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

r_squared = r2_score(y, y_pred)
print(f"R²: {r_squared:.4f}")
print(f"Regression equation: Stock Returns = {model.coef_[0]:.4f} * Index Returns + {model.intercept_:.4f}")

# Plot regression with English labels
plt.figure(figsize=(10, 6))
plt.scatter(merged_df['index_return'], merged_df['daily_return'], alpha=0.3, label='Stock Returns Data')
plt.plot(merged_df['index_return'], y_pred, color='red', label=f'Regression Line: R² = {r_squared:.4f}')
plt.title('Linear Regression: Stock Returns vs. Index Returns', fontsize=16)

# Labels in English
plt.xlabel('Daily Index Returns (S&P 500)', fontsize=12)
plt.ylabel('Daily Stock Returns', fontsize=12)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#-------------------------------------------
#השערה 3
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the cleaned data
stocks_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_stocks_cleaned.csv')
index_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_index_cleaned.csv')
companies_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_companies_cleaned.csv')
final_merged_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_merged_cleaned.csv')

# Ensure correct date format for 'Date' columns in both DataFrames
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'], format='%Y-%m-%d', errors='coerce')
index_df['Date'] = pd.to_datetime(index_df['Date'], format='%Y-%m-%d', errors='coerce')

# Calculate daily returns for stocks
stocks_df['daily_return'] = stocks_df.groupby('symbol')['close'].pct_change()

# Merge stock data with index data on date
merged_df = pd.merge(stocks_df, index_df[['Date', 's&p500']], on='Date', how='inner')

# Merge with companies data on symbol
final_merged_df = pd.merge(merged_df, companies_df, on='symbol', how='left')

# Assign sector types based on the 'sector' column
final_merged_df['sector_type'] = final_merged_df['sector'].apply(
    lambda x: 'Technology' if x == 'Technology' else 'Traditional'
)

# Calculate daily returns for each sector
sector_returns = final_merged_df.groupby('sector_type')['daily_return'].describe()

# Print returns statistics by sector type
print("Returns statistics by sector type:")
print(sector_returns)

# Plot the returns statistics by sector type
plt.figure(figsize=(12, 8))

# Create a bar plot for mean returns
sns.barplot(x=sector_returns.index, y=sector_returns['mean'], palette='viridis')
plt.title('Average Daily Returns by Sector Type', fontsize=16)
plt.xlabel('Sector Type', fontsize=12)
plt.ylabel('Average Daily Return', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Perform t-test to compare returns
technology_returns = final_merged_df[final_merged_df['sector_type'] == 'Technology']['daily_return'].dropna()
traditional_returns = final_merged_df[final_merged_df['sector_type'] == 'Traditional']['daily_return'].dropna()

t_stat, p_value = stats.ttest_ind(technology_returns, traditional_returns, equal_var=False)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("There is a significant difference in average daily returns between technology and traditional sectors.")
else:
    print("There is no significant difference in average daily returns between technology and traditional sectors.")

#-------------------------------------------
#חיזוי מחיר מניות כל החברות שיש בסט הנתונים לפי שנה וחודש שהמשתמש מזין

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Load cleaned data
merged_df = pd.read_csv('C://Users//afnan abed alkreem//Downloads//sp500_merged_cleaned.csv')

# Convert 'Date' column to datetime format
merged_df['Date'] = pd.to_datetime(merged_df['Date'], format='%Y-%m-%d')

# Prepare data for Prophet model
def prepare_prophet_data(symbol, cutoff_date):
    # Filter data by symbol and up to the cutoff date (year-month)
    df = merged_df[(merged_df['symbol'] == symbol) & (merged_df['Date'] <= cutoff_date)]
    
    # Print the data to verify its correctness
    print(f"Data for {symbol} up to {cutoff_date}:")
    print(df[['Date', 'adj_close']].head())
    
    prophet_df = df[['Date', 'adj_close']].rename(columns={'Date': 'ds', 'adj_close': 'y'})
    
    return prophet_df

# Train Prophet model for a specific symbol
def train_prophet_model(symbol, cutoff_date):
    prophet_df = prepare_prophet_data(symbol, cutoff_date)
    
    # Define and fit Prophet model
    model = Prophet(yearly_seasonality=True, daily_seasonality=False)
    model.fit(prophet_df)
    
    return model

# Forecast function for a specific symbol and cutoff date
def generate_forecast_for_symbol(symbol, month, year, days=30):
    cutoff_date = pd.to_datetime(f"{year}-{month}-01")
    
    model = train_prophet_model(symbol, cutoff_date)
    
    # Create future dataframe
    future_dates = pd.date_range(start=cutoff_date, periods=days, freq='D')
    future_df = pd.DataFrame({'ds': future_dates})
    
    # Predict future prices
    forecast = model.predict(future_df)
    
    # Print forecast results
    print(f"Forecast for {symbol}:")
    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
    
    forecast_data = {
        'date': forecast['ds'],
        'predicted_price': forecast['yhat']
    }
    
    forecast_df = pd.DataFrame(forecast_data)
    return forecast_df

# Generate stock forecast for multiple symbols
def generate_stock_forecast(month, year):
    stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    stock_forecast_data = []

    for symbol in stock_symbols:
        forecast_df = generate_forecast_for_symbol(symbol, month, year)
        stock_forecast_data.append({
            'symbol': symbol,
            'predicted_price': forecast_df['predicted_price'].mean()  # Example: using mean predicted price
        })

    stock_forecast_df = pd.DataFrame(stock_forecast_data)
    
    # Print the stock forecast results
    print(f'Stock Forecast Data for {pd.to_datetime(f"{year}-{month}-01").strftime("%B %Y")}:')
    print(stock_forecast_df)
    
    return stock_forecast_df

# Main execution
if __name__ == "__main__":
    year = int(input('Enter Year (2023-2030): '))
    month = int(input('Enter Month (1-12): '))

    # Generate forecast
    stock_forecast_df = generate_stock_forecast(month, year)

    # Display predicted stock prices
    print(f'Predicted Stock Prices for {pd.to_datetime(f"{year}-{month}-01").strftime("%B %Y")}')
    print(stock_forecast_df)

    # Create bar plot for predicted prices
    plt.figure(figsize=(12, 6))
    bars = plt.bar(stock_forecast_df['symbol'], stock_forecast_df['predicted_price'], color='skyblue')
    
    # Add labels to the bars
    for bar in bars:
        height = bar.get_height()
        if height >= 1e9:
            label = f'{height / 1e9:.2f} B'
        elif height >= 1e6:
            label = f'{height / 1e6:.2f} M'
        elif height >= 1e3:
            label = f'{height / 1e3:.2f} K'
        else:
            label = f'{height:.2f}'
        
        plt.text(bar.get_x() + bar.get_width() / 2, height, label, ha='center', va='bottom', fontsize=10)

    plt.xlabel('Stock Symbol')
    plt.ylabel('Predicted Price')
    plt.title(f'Predicted Stock Prices for {pd.to_datetime(f"{year}-{month}-01").strftime("%B %Y")}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

