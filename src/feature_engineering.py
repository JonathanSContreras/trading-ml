import pandas as pd

df = pd.read_csv('../data/AAPL_data.csv', parse_dates=['Date'])

# Target Variable: For each row, I need to answer: did the price go up or down the next trading day?

# next_day_return = (next_day_close - current_day_close) / current_day_close
# target = 1 if next_day_return > 0 else 0

def get_target_variable(df):
    '''
    Function takes a DataFrame with at least a 'Close' column and adds a 'Target' column indicating if the price will go up (1) or down (0) the next trading day.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :return: DataFrame with the new 'Target' column added.
    '''
    df['Next_Day_Close'] = df['Close'].shift(-1) # gets the close price of the next day
    df['Next_Day_Return'] = (df['Next_Day_Close'] - df['Close']) / df['Close'] # calculates the return for the next day
    df['Target'] = (df['Next_Day_Return'] > 0).astype(int) # creates the target variable: 1 if the return is positive, else 0
    return df.drop(columns=['Next_Day_Close', 'Next_Day_Return'])

df_with_target = get_target_variable(df)
# print(df_with_target.head())

# In the case of APPL, this means that on 2024-01-05, the price went up the next day (2024-01-08), so the target is 1.
# On the other hand, on 2024-01-02, the price went down the next day (2024-01-03), so the target is 0.
# Target is a "look-ahead" indicator. It tells you what will happen tomorrow:
    # Target 1: The price is going up tomorrow (Buy / Hold)
    # Target 0: The price is going down tomorrow (Sell / Avoid)

#         Date       Close        High         Low        Open    Volume  Target
# 0 2024-01-02  183.731323  186.502538  181.999316  185.225793  82488700       0
# 1 2024-01-03  182.355606  183.968852  181.544030  182.325916  58414500       0
# 2 2024-01-04  180.039658  181.207518  179.020249  180.277180  71983600       0
# 3 2024-01-05  179.317169  180.880926  178.317559  180.118854  62379700       1
# 4 2024-01-08  183.652145  183.691743  179.633891  180.217821  59144500       0

def daily_returns(df):
    '''
    Function to calculate daily returns from the 'Close' price and add it as a new column 'Daily_Return'.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :return: DataFrame with the new 'Daily_Return' column added.
    '''
    df['Daily_Return'] = df['Close'].pct_change() # calculates the percentage change in close price from the previous day
    return df

df_with_returns = daily_returns(df_with_target)
# print(df_with_returns.head())

# In the case of APPL, the only day with a positive return is 2024-01-08, which is the day after the price went up (2024-01-05). 
# The other days have negative returns, indicating that the price went down compared to the previous day.

#         Date       Close        High         Low        Open    Volume  Target  Daily_Return
# 0 2024-01-02  183.731323  186.502538  181.999316  185.225793  82488700       0           NaN
# 1 2024-01-03  182.355606  183.968852  181.544030  182.325916  58414500       0     -0.007488
# 2 2024-01-04  180.039658  181.207518  179.020249  180.277180  71983600       0     -0.012700
# 3 2024-01-05  179.317169  180.880926  178.317559  180.118854  62379700       1     -0.004013
# 4 2024-01-08  183.652145  183.691743  179.633891  180.217821  59144500       0      0.024175

def multi_day_returns(df, n_days):
    '''
    Function to calculate returns for multiple future days and add them as new columns.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :param n_days: Number of future days to calculate returns for.
    :return: DataFrame with new columns for each future day's return added.
    '''
    for i in range(1, n_days + 1):
        df[f'Return_Day_{i}'] = (df['Close'].shift(-i) - df['Close']) / df['Close'] # calculates the return for the next i days
    return df

df_with_multi_day_returns = multi_day_returns(df_with_target, n_days=5)
# print(df_with_multi_day_returns.head())

# In the case of APPL, the returns for the next 5 days show how the price changed compared to the current day (2024-01-02).
# For example, on 2024-01-02, the return for the next day (2024-01-03) is -0.007488, which means the price went down by approximately 0.75%. 
# The return for the next 5 days (2024-01-08) is -0.002694, indicating a slight decrease in price compared to 2024-01-02, 
# even though there was a positive return on 2024-01-08 itself. This shows the importance of looking at multiple future returns to understand the overall trend and volatility.
# Volatility measures the speed and magnitude of price changes for a security or market index over a specific period. It indicates how "bumpy" an investment's ride is; 
# higher volatility means rapid, dramatic price swings in either direction, representing higher risk and uncertainty, while lower volatility indicates a steadier, more predictable price. 

#         Date       Close        High         Low        Open    Volume  Target  Daily_Return  Return_Day_1  Return_Day_2  Return_Day_3  Return_Day_4  Return_Day_5
# 0 2024-01-02  183.731323  186.502538  181.999316  185.225793  82488700       0           NaN     -0.007488     -0.020093     -0.024025     -0.000431     -0.002694
# 1 2024-01-03  182.355606  183.968852  181.544030  182.325916  58414500       0     -0.007488     -0.012700     -0.016662      0.007110      0.004830      0.010529
# 2 2024-01-04  180.039658  181.207518  179.020249  180.277180  71983600       0     -0.012700     -0.004013      0.020065      0.017756      0.023528      0.020230
# 3 2024-01-05  179.317169  180.880926  178.317559  180.118854  62379700       1     -0.004013      0.024175      0.021857      0.027652      0.024340      0.026162
# 4 2024-01-08  183.652145  183.691743  179.633891  180.217821  59144500       0      0.024175     -0.002264      0.003395      0.000162      0.001940     -0.010401

df_with_multi_day_returns = multi_day_returns(df_with_target, n_days=10)
# print(df_with_multi_day_returns.head())

# In the case of APPL, the returns for the next 10 days provide a more comprehensive view of how the price evolved over a longer period.
# For example, on 2024-01-02, the return for the next 10 days (2024-01-15) is -0.015945, indicating that the price decreased by approximately 1.59% compared to 2024-01-02,
# even though there were some positive returns in between. This highlights the importance of looking at a longer time horizon to understand the overall trend and potential 
# volatility of the stock, as short-term fluctuations may not fully capture the stock's performance over time.

#         Date       Close        High         Low        Open    Volume  Target  Daily_Return  Return_Day_1  Return_Day_2  Return_Day_3  Return_Day_4  Return_Day_5  Return_Day_6  Return_Day_7  Return_Day_8  Return_Day_9  Return_Day_10
# 0 2024-01-02  183.731323  186.502538  181.999316  185.225793  82488700       0           NaN     -0.007488     -0.020093     -0.024025     -0.000431     -0.002694      0.002963     -0.000269      0.001508     -0.010827      -0.015945
# 1 2024-01-03  182.355606  183.968852  181.544030  182.325916  58414500       0     -0.007488     -0.012700     -0.016662      0.007110      0.004830      0.010529      0.007273      0.009064     -0.003365     -0.008521       0.023772
# 2 2024-01-04  180.039658  181.207518  179.020249  180.277180  71983600       0     -0.012700     -0.004013      0.020065      0.017756      0.023528      0.020230      0.022044      0.009455      0.004233      0.036941       0.053048
# 3 2024-01-05  179.317169  180.880926  178.317559  180.118854  62379700       1     -0.004013      0.024175      0.021857      0.027652      0.024340      0.026162      0.013523      0.008279      0.041119      0.057291       0.070151
# 4 2024-01-08  183.652145  183.691743  179.633891  180.217821  59144500       0      0.024175     -0.002264      0.003395      0.000162      0.001940     -0.010401     -0.015521      0.016544      0.032334      0.044891       0.051843