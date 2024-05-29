import pandas as pd
import os

# Load Nasdaq Stock list
def get_nasdaq():
    cwd = os.getcwd()
    file_path = os.path.join(cwd,'data', 'nasdaq_screener_1711467065464.csv')
    df = pd.read_csv(file_path)
    return df

#Separate in to ticker list and stock name list
def get_symbol_list(df):
    symbol_list = [str(symbol).upper() if not pd.isna(symbol) else '' for symbol in df['Symbol'].tolist()]
    return symbol_list

def get_name_list(df):
    name_list = [name.lower() for name in df['Name'].tolist()]
    return name_list
