## app.py
import streamlit as st
from datetime import datetime
from typing import Tuple
from pandas import DataFrame
from data_fetcher import DataFetcher
from data_visualizer import DataVisualizer

class App:
    def __init__(self, date_range: Tuple[datetime, datetime], ticker_symbol: str = 'AAPL'):
        self.date_range = date_range
        self.ticker_symbol = ticker_symbol
        self.stock_data = None

    def run(self):
        st.title('Stock Market Indices Visualization')
        
        # User input for date range
        start_date, end_date = st.date_input(
            "Select date range",
            [self.date_range[0], self.date_range[1]]
        )
        self.date_range = (start_date, end_date)
        
        self.fetch_data()
        self.visualize_data()

    def fetch_data(self):
        data_fetcher = DataFetcher(self.date_range, self.ticker_symbol)
        self.stock_data = data_fetcher.fetch_data()
        if self.stock_data is None:
            st.error('Failed to fetch data.')
            return

    def visualize_data(self):
        if self.stock_data is not None:
            data_visualizer = DataVisualizer(self.stock_data)
            figure = data_visualizer.visualize_data()
            if figure is not None:
                st.plotly_chart(figure)
            else:
                st.error('Failed to visualize data.')
        else:
            st.error('No data to visualize.')

if __name__ == '__main__':
    default_date_range = (datetime(2020, 1, 1), datetime(2021, 12, 31))
    app = App(default_date_range)
    app.run()
