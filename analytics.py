import pandas as pd
import matplotlib.pyplot as plt
from fetch_api import get_info_stock

data = get_info_stock("GOOG")

class Graph:

    def __init__(self, title):
        self.__data = ["Date","Open","High","Low","Close","Volume","Dividends","Stock Splits"]
        plt.figure(figsize=(18, 8))
        plt.title(title)

    def add_data(self, dat):
        if dat not in self.__data:
            raise Exception("Invalid data")
        plt.plot(data[dat], label=f'{dat} Price', color='blue')

    def add_SMA(self, dat, **windows):
        if dat not in self.__data:
            raise Exception("Invalid data")
        for _, size in windows.items():
            data[f"SMA_{size}"] = data[dat].rolling(window=size).mean()
        for colour, size in windows.items():
            plt.plot(data[f"SMA_{size}"], label=f'{size}-Day SMA', color=colour)

    def add_EMA(self, dat, **windows):
        if dat not in self.__data:
            raise Exception("Invalid data")
        for _, size in windows.items():
            data[f"EMA_{size}"] = data[dat].ewm(span=size, adjust=False).mean()
        for colour, size in windows.items():
            plt.plot(data[f"EMA_{size}"], label=f'{size}-Day EMA', color=colour)
    
    def add_RSI(self, dat, w):
        if dat not in self.__data:
            raise Exception("Invalid data")
        delta = data[dat].diff(1)
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        average_gain = gain.rolling(window=w).mean()
        average_loss = loss.rolling(window=w).mean()

        rs = average_gain / average_loss
        data['RSI'] = 100 - (100 / (1 + rs))

        plt.plot(data['RSI'], label='RSI', color='purple')
        plt.axhline(70, color='red', linestyle='--', label='Overbought')
        plt.axhline(30, color='green', linestyle='--', label='Oversold')

    def add_MACD(self, dat):
        data['MACD'] = data[dat].ewm(span=12, adjust=False).mean() - data[dat].ewm(span=26, adjust=False).mean()
        data['Signal Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

        plt.plot(data['MACD'], label='MACD', color='blue')
        plt.plot(data['Signal Line'], label='Signal Line', color='red')
        plt.bar(data.index, data['MACD'] - data['Signal Line'], color='gray', alpha=0.3, label='Histogram')

    def show(self):
        plt.legend()
        plt.show()

graph = Graph("Simple Moving Average (SMA)")
graph.add_SMA("Close",red=20,green=50)
#graph.add_EMA("Close",purple=20,black=50)
#graph.add_RSI("Close",20)
#graph.add_MACD("Close")
graph.add_data("High")
graph.show()