
import pandas as pd


class Stock:
    def __init__(self, stock_symbol, stock_type, last_dividend, fixed_dividend, par_value):
        self.symbol = stock_symbol
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value

    def calculate_dividend_yield(self, price):
        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        if self.stock_type == "Common":
            return self.last_dividend / price
        elif self.stock_type == "Preferred":
            return (self.fixed_dividend * self.par_value) / price
        else:
            raise ValueError("Invalid stock type.")

    def calculate_pe_ratio(self, price):
        dividend = self.calculate_dividend_yield(price)
        if dividend == 0:
            return float('nan')
        return price / dividend

    @staticmethod
    def load_stocks_from_csv(filepath):
        df = pd.read_csv(filepath)
        df['Fixed_Dividend'] = (
            df['Fixed_Dividend']
            .astype(str)
            .str.rstrip('%')
            .replace('nan', '')
            .replace('', '0')
            .astype(float) / 100
        )
        return [Stock(row['Stock Symbol'], row['Type'], row['Last_Dividend'], row['Fixed_Dividend'], row['Par_Value'])
                for _, row in df.iterrows()]
