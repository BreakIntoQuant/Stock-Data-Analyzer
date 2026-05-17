from data_loader import fetch_stock_data

from indicators import (
    calculate_daily_returns,
    calculate_moving_averages
)

from visualization import plot_stock_data


def main():

    ticker = "AAPL"

    start_date = "2020-01-01"
    end_date = "2025-01-01"

    data = fetch_stock_data(
        ticker,
        start_date,
        end_date
    )

    data = calculate_daily_returns(data)

    data = calculate_moving_averages(data)

    print(data.head())

    print("\nSummary Statistics:\n")

    print(data.describe())

    plot_stock_data(data, ticker)


if __name__ == "__main__":
    main()