from DATAPREP.loaddata import get_nasdaq, get_symbol_list, get_name_list
from DATAREDDIT.redditinfo import reddit_init, wsb_daily_comms, title_post_ticker
from DATAVIS.graphs import barplot

# load data from the nasdaq
print('load nasdaq info')
nasdaq_df = get_nasdaq()

# get list of ticker symbols
ticker_list = get_symbol_list(nasdaq_df)

# initialise reddit connection
print('connecting with reddit')
reddit = reddit_init()

# # get list of stocks
# stock_disc = wsb_daily_comms(reddit, ticker_list, 0)

# get list of tickers from posts (no comments)
sub_list=('wallstreetbets', 'investing', 'stocks')
print('Collecting tickers from post titles and text')
test = title_post_ticker(reddit, sub_list, ticker_list, 50)
print(test)
barplot(test)
