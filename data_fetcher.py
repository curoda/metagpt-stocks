## data_fetcher.py
import yfinance as yf
from typing import Tuple
from datetime import datetime
from pandas import DataFrame

class DataFetcher:
    def __init__(self, date_range: Tuple[datetime, datetime], ticker_symbol: str = 'AAPL'):
        self.date_range = date_range
        self.ticker_symbol = ticker_symbol

    def fetch_data(self) -> DataFrame:
        try:
            ticker = yf.Ticker(self.ticker_symbol)
            data = ticker.history(start=self.date_range[0], end=self.date_range[1])
            return data
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")
            return None
