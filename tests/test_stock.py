import unittest
from stock_market.stock import Stock


class TestStock(unittest.TestCase):
    def test_dividend_yield_common(self):
        stock = Stock("POP", "Common", 8, None, 100)
        self.assertAlmostEqual(stock.calculate_dividend_yield(10), 0.8)

    def test_dividend_yield_preferred(self):
        stock = Stock("GIN", "Preferred", 8, 0.02, 100)
        self.assertAlmostEqual(stock.calculate_dividend_yield(10), 0.2)

    def test_pe_ratio(self):
        stock = Stock("ALE", "Common", 23, None, 60)
        self.assertAlmostEqual(stock.calculate_pe_ratio(10), 10 / stock.calculate_dividend_yield(10))
