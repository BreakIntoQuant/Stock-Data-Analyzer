def calculate_daily_returns(data):

    data['Daily Return'] = data['Close'].pct_change()

    return data


def calculate_moving_averages(
    data,
    short_window=20,
    long_window=50
):

    data[f'SMA_{short_window}'] = (
        data['Close']
        .rolling(window=short_window)
        .mean()
    )

    data[f'SMA_{long_window}'] = (
        data['Close']
        .rolling(window=long_window)
        .mean()
    )

    return data