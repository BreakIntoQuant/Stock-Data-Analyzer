import matplotlib.pyplot as plt


def plot_stock_data(data, ticker):

    plt.figure(figsize=(14, 7))

    plt.plot(
        data['Close'],
        label='Close Price',
        linewidth=2
    )

    if 'SMA_20' in data.columns:
        plt.plot(data['SMA_20'], label='20-Day SMA')

    if 'SMA_50' in data.columns:
        plt.plot(data['SMA_50'], label='50-Day SMA')

    plt.title(f'{ticker} Stock Price Analysis')

    plt.xlabel('Date')
    plt.ylabel('Price ($)')

    plt.legend()

    plt.grid(True)

    plt.savefig(f'charts/{ticker}_analysis.png')

    plt.show()