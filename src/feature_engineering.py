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
print(df_with_target.head())

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