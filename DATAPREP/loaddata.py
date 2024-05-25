import pandas as pd
import os

# Load Nasdaq Stock list
cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
file_path = os.path.join(parent_dir,'data', 'nasdaq_screener_1711467065464.csv')
df = pd.read_csv(file_path)

#Separate in to ticker list and stock name list
symbol_list = [str(symbol).upper() if not pd.isna(symbol) else '' for symbol in df['Symbol'].tolist()]
name_list = [name.lower() for name in df['Name'].tolist()]

print(symbol_list)
