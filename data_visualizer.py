## data_visualizer.py
import plotly.graph_objects as go
from pandas import DataFrame
from plotly.graph_objs import Figure

class DataVisualizer:
    def __init__(self, data: DataFrame):
        self.data = data

    def visualize_data(self) -> Figure:
        try:
            fig = go.Figure()
            if 'Close' in self.data.columns:
                fig.add_trace(go.Scatter(x=self.data.index, y=self.data['Close'], mode='lines', name='Close'))
            if 'Open' in self.data.columns:
                fig.add_trace(go.Scatter(x=self.data.index, y=self.data['Open'], mode='lines', name='Open'))
            fig.update_layout(title='Stock Market Data', xaxis_title='Date', yaxis_title='Price')
            return fig
        except Exception as e:
            print(f"An error occurred while visualizing data: {e}")
            return None
