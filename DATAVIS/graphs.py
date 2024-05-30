import matplotlib.pyplot as plt

def barplot(data):
    ticker = (data.keys())
    count = (data.values())
    plt.figure(figsize =(12,6))
    plt.bar(ticker, count)
    plt.xlabel('Tickers')
    plt.ylabel('Frequency')
    plt.title('Frequency of Tickers from Reddit')
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show
