import yfinance as yf

def get_info_stock(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period='max')
    hist.to_csv(f"api/{ticker}.csv")

get_info_stock("GOOG")