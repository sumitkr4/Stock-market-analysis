import unittest
from stock_market.stock import Stock
from stock_market.trade import Trade


class TestTrade(unittest.TestCase):
    def test_trade_creation(self):
        stock = Stock("POP", "Common", 8, None, 100)
        trade = Trade(stock, 100, "Buy", 10)
        self.assertEqual(trade.stock.symbol, "POP")
        self.assertEqual(trade.quantity, 100)
        self.assertEqual(trade.buy_sell, "Buy")
        self.assertEqual(trade.price, 10)