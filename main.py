from DATAPREP.loaddata import get_nasdaq, get_symbol_list, get_name_list, get_symbol_list_mc
from DATAREDDIT.redditinfo import reddit_init, wsb_daily_comms, title_post_ticker
from DATAVIS.graphs import bar_plot

wsb_daily = ''
while wsb_daily != 'y' and wsb_daily != 'n':
    wsb_daily = input('Get wsb daily discussion tickers. [y/n]')

title_post = ''
while title_post != 'y' and title_post != 'n':
    title_post = input('Get tickers from posts. [y/n]')

# load data from the nasdaq
print('load nasdaq info')
nasdaq_df = get_nasdaq()
print('Done')

# get list of ticker symbols
ticker_list = get_symbol_list_mc(nasdaq_df)

# initialise reddit connection
print('connecting with reddit')
reddit = reddit_init()

# # get list of stocks
# stock_disc = wsb_daily_comms(reddit, ticker_list, 0)

# get tickers from wsb daily discussion comments
if wsb_daily == 'y':
    print('going through comments')
    com_wsb = wsb_daily_comms(reddit, 5)
    print(com_wsb)

# get list of tickers from posts (no comments)
if title_post == 'y':
    sub_list=('wallstreetbets', 'investing', 'stocks')
    print('Collecting tickers from post titles and text')
    data = title_post_ticker(reddit, sub_list, ticker_list, 50)
    print(data)
    bar_plot(data)
