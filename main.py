from stock_market.stock import Stock
from stock_market.trade import Trade
from stock_market.market import StockMarket

# Load stocks from CSV
stocks = Stock.load_stocks_from_csv("data/stocks.csv")
market = StockMarket()

# Record some trades
market.record_trade(Trade(stocks[1], 100, "Buy", 10))
market.record_trade(Trade(stocks[2], 50, "Sell", 15))
market.record_trade(Trade(stocks[3], 200, "Buy", 25))

# Choose stock to analyze
for stock in stocks:
    print(f"\nStock: {stock.symbol}")

    price = 10  # Example price

    # Dividend Yield is calculated for all stocks
    print("Dividend Yield:", stock.calculate_dividend_yield(price))

    # P/E Ratio is calculated for all stocks
    print("P/E Ratio:", stock.calculate_pe_ratio(price))

    # Compute volume weighted stock price
    print("Volume Weighted Stock Price:", market.calculate_vwsp(stock))

    print()

# # Compute GBCE Index for all stocks
gbce_index = market.calculate_gbce_index()
if gbce_index > 0:
    print("\nGBCE Index:", gbce_index)
