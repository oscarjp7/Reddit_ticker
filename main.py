from DATAPREP.loaddata import get_nasdaq, get_symbol_list, get_name_list
from DATAREDDIT.redditinfo import reddit_init, daily_comms

# load data from the nasdaq
nasdaq_df = get_nasdaq()

# get list of ticker symbols
ticker_list = get_symbol_list(nasdaq_df)

# initialise reddit connection
reddit = reddit_init()

# get list of stocks
stock_disc = daily_comms(reddit, ticker_list)

print(stock_disc)
