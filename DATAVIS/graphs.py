import matplotlib.pyplot as plt

def bar_plot(data):
    ticker = (data.keys())
    print(ticker)
    count = (data.values())
    plt.figure(figsize =(12,6))
    plt.bar(ticker, count)
    plt.xlabel('Tickers')
    plt.ylabel('Frequency')
    plt.title('Frequency of Tickers from Reddit')
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show
