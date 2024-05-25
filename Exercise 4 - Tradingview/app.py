import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output

# Fetch historical stock data
def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="1y")  # Fetch 1 year of historical data
    return df

# Initialize Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("TradingView Clone"),
    dcc.Input(id="ticker-input", value="AAPL", type="text"),
    dcc.Graph(id="stock-chart"),
    dcc.Interval(id="interval-component", interval=60*1000, n_intervals=0)  # Update every minute
])

@app.callback(
    Output("stock-chart", "figure"),
    Input("ticker-input", "value"),
    Input("interval-component", "n_intervals")
)
def update_chart(ticker, n):
    df = fetch_data(ticker)
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close'],
                                 name='market data'))
    fig.update_layout(title=f'{ticker} Stock Price', yaxis_title='Price (USD)')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
