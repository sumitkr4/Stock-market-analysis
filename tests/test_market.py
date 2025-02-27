import unittest
from stock_market.stock import Stock
from stock_market.trade import Trade
from stock_market.market import StockMarket


class TestStockMarket(unittest.TestCase):
    def test_vwsp(self):
        stock = Stock("POP", "Common", 8, None, 100)
        market = StockMarket()
        trade1 = Trade(stock, 100, "Buy", 10)
        trade2 = Trade(stock, 200, "Sell", 20)
        market.record_trade(trade1)
        market.record_trade(trade2)

        self.assertAlmostEqual(market.calculate_vwsp(stock), (10 * 100 + 20 * 200) / 300)

    def test_gbce_index(self):
        stock1 = Stock("POP", "Common", 8, None, 100)
        stock2 = Stock("ALE", "Common", 23, None, 60)
        market = StockMarket()
        market.record_trade(Trade(stock1, 100, "Buy", 10))
        market.record_trade(Trade(stock2, 200, "Sell", 20))

        self.assertGreater(market.calculate_gbce_index(), 0)