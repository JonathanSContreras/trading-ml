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

# Basic Return Features: Daily returns and multi-day returns can provide insights into the stock's performance and volatility.

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

# Moving Averages Features: # Moving averages are commonly used in trading to smooth out price data and identify trends. They can be calculated over different time periods 
# (e.g., 5-day, 10-day, 20-day) to capture short-term and long-term trends.
# For example, a 5-day moving average is calculated by taking the average of the closing prices over the last 5 days. This can help identify the direction of the trend and 
# potential support or resistance levels. A common strategy is to look for crossovers between short-term and long-term moving averages (e.g., 5-day crossing above 20-day)
# as potential buy or sell signals.
# Note: The useful feature isn't the MA itself, but it's price relative to the MA (e.g., is price above or below the 50-day MA? By how much?)
def simple_moving_average(df, window=5):
    '''
    Function to calculate the moving average of the 'Close' price and add it as a new column.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :param window: The number of days to calculate the moving average over.
    :return: DataFrame with the new moving average column added.
    '''
    df[f'MA_{window}'] = df['Close'].rolling(window=window).mean() # calculates the moving average for the specified window
    return df

# print(simple_moving_average(df_with_multi_day_returns, window=20).head(50))
# In the case of APPL, the 20-day moving average (MA_20) provides a smoothed line that represents the average closing price over the last 20 days.
# For example, on 2024-01-30, the MA_20 is 185.958668, which means that the average closing price of APPL over the last 20 days was approximately $185.96. 
# This can help identify the overall trend of the stock. If the current price is above the MA_20, it may indicate an uptrend, while if the current price is below the MA_20, it may indicate a downtrend.
# We can use this information to make informed trading decisions, such as buying when the price crosses above the MA_20 or selling when it crosses below. 
# However, it's important to consider other factors and indicators in conjunction with moving averages for a more comprehensive analysis.
#          Date       Close        High         Low        Open     Volume  Target  Daily_Return  Return_Day_1  Return_Day_2  Return_Day_3  Return_Day_4  Return_Day_5  Return_Day_6  Return_Day_7  Return_Day_8  Return_Day_9  Return_Day_10       MA_20
# 0  2024-01-02  183.731323  186.502538  181.999316  185.225793   82488700       0           NaN     -0.007488     -0.020093     -0.024025     -0.000431     -0.002694      0.002963     -0.000269      0.001508     -0.010827      -0.015945         NaN
# 1  2024-01-03  182.355606  183.968852  181.544030  182.325916   58414500       0     -0.007488     -0.012700     -0.016662      0.007110      0.004830      0.010529      0.007273      0.009064     -0.003365     -0.008521       0.023772         NaN
# 2  2024-01-04  180.039658  181.207518  179.020249  180.277180   71983600       0     -0.012700     -0.004013      0.020065      0.017756      0.023528      0.020230      0.022044      0.009455      0.004233      0.036941       0.053048         NaN
# 3  2024-01-05  179.317169  180.880926  178.317559  180.118854   62379700       1     -0.004013      0.024175      0.021857      0.027652      0.024340      0.026162      0.013523      0.008279      0.041119      0.057291       0.070151         NaN
# 4  2024-01-08  183.652145  183.691743  179.633891  180.217821   59144500       0      0.024175     -0.002264      0.003395      0.000162      0.001940     -0.010401     -0.015521      0.016544      0.032334      0.044891       0.051843         NaN
# 5  2024-01-09  183.236435  183.246327  180.851210  182.028977   42841800       1     -0.002264      0.005671      0.002431      0.004213     -0.008156     -0.013287      0.018851      0.034676      0.047262      0.054229       0.050556         NaN
# 6  2024-01-10  184.275650  184.483482  182.028985  182.454572   46792900       0      0.005671     -0.003222     -0.001450     -0.013749     -0.018852      0.013105      0.028841      0.041356      0.048284      0.044632       0.042859         NaN
# 7  2024-01-11  183.681824  185.126819  181.732077  184.622053   49128400       1     -0.003222      0.001778     -0.010561     -0.015680      0.016380      0.032168      0.044722      0.051673      0.048009      0.046231       0.036802         NaN
# 8  2024-01-12  184.008438  184.820014  183.285948  184.146998   40477800       0      0.001778     -0.012317     -0.017427      0.014576      0.030335      0.042868      0.049806      0.046149      0.044374      0.034961       0.031250         NaN
# 9  2024-01-16  181.742004  182.365517  179.069752  180.287117   65603000       0     -0.012317     -0.005174      0.027229      0.043184      0.055873      0.062898      0.059195      0.057398      0.047868      0.044110       0.024015         NaN
# 10 2024-01-17  180.801743  181.049172  178.446223  179.406251   47317400       1     -0.005174      0.032571      0.048609      0.061364      0.068426      0.064703      0.062897      0.053317      0.049540      0.029341       0.009415         NaN
# 11 2024-01-18  186.690567  187.195318  183.919353  184.176674   78005800       1      0.032571      0.015533      0.027885      0.034724      0.031119      0.029370      0.020092      0.016434     -0.003128     -0.022425      -0.009383         NaN
# 12 2024-01-19  189.590424  189.976413  186.878605  187.383356   68903000       1      0.015533      0.012163      0.018897      0.015348      0.013625      0.004490      0.000888     -0.018376     -0.037377     -0.024535      -0.029808         NaN
# 13 2024-01-22  191.896484  193.321681  190.283239  190.322836   60133900       1      0.012163      0.006653      0.003146      0.001444     -0.007582     -0.011140     -0.030172     -0.048945     -0.036258     -0.041467      -0.032029         NaN
# 14 2024-01-23  193.173203  193.737349  191.837092  193.014859   42355600       0      0.006653     -0.003484     -0.005175     -0.014141     -0.017676     -0.036582     -0.055231     -0.042627     -0.047802     -0.038426      -0.030126         NaN
# 15 2024-01-24  192.500198  194.360873  192.341840  193.410737   53631300       0     -0.003484     -0.001697     -0.010694     -0.014242     -0.033213     -0.051928     -0.039280     -0.044473     -0.035064     -0.026735      -0.026169         NaN
# 16 2024-01-25  192.173584  194.251998  191.124485  193.212791   54822100       0     -0.001697     -0.009013     -0.012566     -0.031570     -0.050317     -0.037647     -0.042849     -0.033424     -0.025081     -0.024514      -0.030128         NaN
# 17 2024-01-26  190.441605  192.757542  189.966544  192.272590   44594000       0     -0.009013     -0.003586     -0.022763     -0.041680     -0.028895     -0.034144     -0.024634     -0.016214     -0.015643     -0.021308      -0.017301         NaN
# 18 2024-01-29  189.758698  190.223866  187.630809  190.035817   47145600       0     -0.003586     -0.019246     -0.038231     -0.025400     -0.030668     -0.021124     -0.012674     -0.012100     -0.017785     -0.013764      -0.022642         NaN
# 19 2024-01-30  186.106598  189.827948  185.542466  188.976790   55859400       0     -0.019246     -0.019357     -0.006275     -0.011646     -0.001914      0.006701      0.007286      0.001489      0.005589     -0.003463      -0.014698  185.958668
# 20 2024-01-31  182.504074  185.176326  182.454600  185.116930   55467800       1     -0.019357      0.013341      0.007863      0.017787      0.026573      0.027169      0.021258      0.025439      0.016208      0.004751      -0.000081  185.897305
# 21 2024-02-01  184.938782  185.027853  181.930044  182.098295   64885400       0      0.013341     -0.005405      0.004388      0.013058      0.013647      0.007813      0.011939      0.002830     -0.008476     -0.013245      -0.014799  186.026464
# print(simple_moving_average(df_with_multi_day_returns, window=100).head(200))

# Indicators (RSI, MACD, Bollinger Bands, etc.): 
    # These technical indicators can help identify trends, momentum, and potential reversal points in the stock price.

# RSI (Relative Strength Index): Measures the speed and change of price movements to identify overbought or oversold conditions.
# This is helpful to identify potential reversal points in the stock price. An RSI above 70 typically indicates that the stock is overbought, 
# suggesting a potential reversal or pullback in price, while an RSI below 30 indicates that the stock is oversold, suggesting a potential buying opportunity or a reversal to the upside.

# Steps to Calculate RSI:
# 1. Determine Period: 
    # Choose a time period (commonly 14 days).
# 2. Calculate Gains and Losses: 
    # For each day, calculate the gain (if the price went up) or loss (if the price went down) compared to the previous day.
    # Gains are positive, and losses are negative. If the price didn't change, both gain and loss are zero.
# 3. Initial Average Gain and Loss: 
    # For the first 14 days, calculate the average gain and average loss by summing the gains and losses over the period and dividing by 14.
# 4. Calculate RS (Relative Strength): 
    # RS = Average Gain / Average Loss. This ratio indicates the strength of the price movement.
# 5. Calculate RSI: 
    # RSI = 100 - (100 / (1 + RS)). This formula converts the RS value into a scale from 0 to 100, where values above 70 typically indicate overbought conditions and values below 30 indicate oversold conditions.
# 6. Subsequent Average (Smoothing):
    # For subsequent periods, use a smoothing technique to prevent sudden spikes or drops in the RSI value.
    # Average Gain = [(Previous Average Gain * (n-1)) + Current Gain] / n
    # Average Loss = [(Previous Average Loss * (n-1)) + Current Loss] / n

# Key interpretation of RSI:
# - RSI above 70: The stock is considered overbought, which may indicate a potential reversal or pullback in price.
# - RSI below 30: The stock is considered oversold, which may indicate a potential buying opportunity or a reversal to the upside.
# - RSI Near 50: The stock is considered to be in a neutral zone, where there is no clear indication of being overbought or oversold.

def relative_strength_index(df, window=14):
    '''
    Function to calculate the Relative Strength Index (RSI) and add it as a new column.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :param window: The number of days to calculate the RSI over (commonly 14).
    :return: DataFrame with the new RSI column added.
    '''
    delta = df['Close'].diff() # calculates the difference in close price from the previous day
    gain = delta.where(delta > 0, 0) # keeps gains and sets losses to 0
    loss = -delta.where(delta < 0, 0) # keeps losses and sets gains to 0
    avg_gain = gain.rolling(window=window).mean() # calculates the average gain over the specified window
    avg_loss = loss.rolling(window=window).mean() # calculates the average loss over the specified window
    # subsequent average (smoothing) for gains and losses
    avg_gain = avg_gain.shift(1) * (window - 1) / window + gain / window # applies smoothing to the average gain
    avg_loss = avg_loss.shift(1) * (window - 1) / window + loss / window # applies smoothing to the average loss
    rs = avg_gain / avg_loss # calculates the relative strength
    df[f'RSI_{window}'] = 100 - (100 / (1 + rs)) # calculates the RSI and adds it as a new column
    return df

# print(relative_strength_index(df_with_multi_day_returns, window=14).head(50))

# MACD (Moving Average Convergence Divergence): Shows the relationship between two moving averages of a stock's price to identify potential buy or sell signals.
# This is helpful to identify changes in the strength, direction, momentum, and duration of a trend in a stock's price. 
# Which helps traders time entries and exits by identifying momentum shifts and trend reversals before they are fully reflected in the price.

# Steps to calculate MACD:
# 1. Calculate the Short-Term EMA:
    # Choose a short-term period (commonly 12 days) and calculate the Exponential Moving Average (EMA) of the closing price over that period. The EMA gives more weight to recent prices, making it more responsive to recent price changes.
# 2. Calculate the Long-Term EMA:
    # Choose a long-term period (commonly 26 days) and calculate the EMA of the closing price over that period.
# 3. Calculate the MACD Line:
    # MACD Line = Short-Term EMA - Long-Term EMA. This line represents the difference between the two EMAs and indicates the momentum of the stock. A positive MACD line suggests that the short-term EMA is above the long-term EMA, indicating upward momentum, while a negative MACD line suggests downward momentum.
# 4. Calculate the Signal Line:
    # Choose a signal period (commonly 9 days) and calculate the EMA of the MACD line over that period. The Signal Line is used to generate buy or sell signals based on crossovers with the MACD line.

def moving_average_convergence_divergence(df, short_window=12, long_window=26, signal_window=9):
    '''
    Function to calculate the Moving Average Convergence Divergence (MACD) and add it as new columns.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :param short_window: The number of days for the short-term EMA (commonly 12).
    :param long_window: The number of days for the long-term EMA (commonly 26).
    :param signal_window: The number of days for the signal line EMA (commonly 9).
    :return: DataFrame with new columns for MACD and Signal Line added.
    '''
    df[f'EMA_{short_window}'] = df['Close'].ewm(span=short_window, adjust=False).mean() # calculates the short-term EMA
    df[f'EMA_{long_window}'] = df['Close'].ewm(span=long_window, adjust=False).mean() # calculates the long-term EMA
    df['MACD'] = df[f'EMA_{short_window}'] - df[f'EMA_{long_window}'] # calculates the MACD line
    df['Signal_Line'] = df['MACD'].ewm(span=signal_window, adjust=False).mean() # calculates the signal line
    return df

# print(moving_average_convergence_divergence(df_with_multi_day_returns, short_window=12, long_window=26, signal_window=9).head(50))

# Bollinger Bands: Consist of a moving average and two standard deviation lines above and below it, indicating volatility and potential price breakouts.
# Bollinger Bands are calculated using a 20-period simple moving average (SMA) as the middle band, with upper and lower bands set at two standard deviations above and below it. 
# The bands expand with higher volatility and contract during calmer markets. They are computed using closing prices for a specified period (typically 20 days). 

# Steps to calculate Bollinger Bands:
# 1. Calculate the Middle Band (SMA):
    # Calculate the 20-day Simple Moving Average (SMA) of the closing prices.
# 2. Calculate the Standard Deviation (SD):
    # Find the standard deviation of the same 20-day closing prices. This measures how much the prices deviate from the average.
# 3. Calculate the Upper and Lower Bands:
    # Upper Band = Middle Band + (2 * SD)
    # Lower Band = Middle Band - (2 * SD)

def bollinger_bands(df, window=20):
    '''
    Function to calculate Bollinger Bands and add them as new columns.
    :param df: DataFrame containing at least a 'Close' column with daily closing prices.
    :param window: The number of days to calculate the moving average and standard deviation over (commonly 20).
    :return: DataFrame with new columns for Middle Band, Upper Band, and Lower Band added.
    '''
    df[f'Middle_Band_{window}'] = simple_moving_average(df, window)[f'MA_{window}'] # calculates the middle band using the simple moving average
    df[f'Standard_Deviation_{window}'] = df['Close'].rolling(window=window).std() # calculates the standard deviation
    df[f'Upper_Band_{window}'] = df[f'Middle_Band_{window}'] + (2 * df[f'Standard_Deviation_{window}']) # calculates the upper band
    df[f'Lower_Band_{window}'] = df[f'Middle_Band_{window}'] - (2 * df[f'Standard_Deviation_{window}']) # calculates the lower band
    return df

bollinger_bands(df_with_multi_day_returns, window=20)

# Volume Indicators: Volume is a crucial aspect of trading, and indicators like On-Balance Volume (OBV) or Volume Weighted Average Price (VWAP) can provide insights into the strength of price movements and potential reversals.