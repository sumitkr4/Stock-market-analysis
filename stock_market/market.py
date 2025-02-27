
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


class StockMarket:
    def __init__(self):
        self.trades = pd.DataFrame(columns=['Stock_Symbol', 'timestamp', 'quantity', 'buy_sell', 'price']).astype({
            'Stock_Symbol': str,
            'timestamp': 'datetime64[ns]',
            'quantity': int,
            'buy_sell': str,
            'price': float
        })

    def record_trade(self, trade):
        new_trade = pd.DataFrame([{
            'Stock_Symbol': trade.stock.symbol,
            'timestamp': trade.timestamp,
            'quantity': trade.quantity,
            'buy_sell': trade.buy_sell,
            'price': trade.price
        }])

        self.trades = pd.concat([self.trades, new_trade], ignore_index=True)

    def calculate_vwsp(self, stock):
        now = datetime.now()
        self.trades['timestamp'] = pd.to_datetime(self.trades['timestamp'])
        relevant_trades = self.trades[(self.trades['Stock_Symbol'] == stock.symbol) & 
                                      (self.trades['timestamp'] > now - timedelta(minutes=5))]
        if relevant_trades.empty:
            return 0
        return (relevant_trades['price'] * relevant_trades['quantity']).sum() / relevant_trades['quantity'].sum()

    def calculate_gbce_index(self):
        if self.trades.empty:
            return 0

        self.trades['price'] = pd.to_numeric(self.trades['price'], errors='coerce')
        valid_prices = self.trades['price'].dropna().values

        valid_prices = valid_prices[valid_prices > 0]

        if len(valid_prices) == 0:
            return 0

        return np.exp(np.mean(np.log(valid_prices)))
