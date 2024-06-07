import pandas as pd
import os

# Load Nasdaq Stock list
def get_nasdaq():
    cwd = os.getcwd()
    file_path = os.path.join(cwd,'data', 'nasdaq_screener_1711467065464.csv')
    df = pd.read_csv(file_path)
    return df

# Separate in to ticker list and stock name list
def get_symbol_list(df):
    symbol_list = [str(symbol).upper() if not pd.isna(symbol) else '' for symbol in df['Symbol'].tolist()]
    return symbol_list

def get_name_list(df):
    name_list = [name.lower() for name in df['Name'].tolist()]
    return name_list

# Get list with market cap over 10e+6
def get_symbol_list_mc(df):
    filtered_df = df[df['Market Cap'] > 100000000]
    symbol_list = [str(symbol).upper() if not pd.isna(symbol) else '' for symbol in filtered_df['Symbol'].tolist()]
    return symbol_list

def get_name_list_mc(df):
    name_list = [name.lower() for name in df['Name'].tolist()]
    return name_list

def get_ticker_and_name(df):
    symbol_name_dict = {}
    for index, row in df.iterrows():
        symbol = str(row['Symbol']).upper() if not pd.isna(row['Symbol']) else ''
        name = row['Name'].lower()

        # Only add to the dictionary if symbol is not empty
        if symbol:
            symbol_name_dict[name] = symbol

    return symbol_name_dict
