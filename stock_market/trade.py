from datetime import datetime


class Trade:
    def __init__(self, stock, quantity, buy_sell, price):
        self.timestamp = datetime.now()
        self.stock = stock
        self.quantity = quantity
        self.buy_sell = buy_sell
        self.price = price

