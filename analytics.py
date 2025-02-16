import pandas as pd
import matplotlib.pyplot as plt
from fetch_api import get_info_stock

data = get_info_stock("GOOG")

class Display_Graph:

    def __init__(self, title):
        self.__data = ["Date","Open","High","Low","Close","Volume","Dividends","Stock Splits"]
        plt.figure(figsize=(18, 8))
        plt.title(title)

    def add_data(self, dat):
        if dat not in self.__data:
            raise Exception("Invalid data")
        plt.plot(data[dat], label=f'{dat} Price', color='blue')

    def add_SMA(self, dat, **windows): # Windows -> {size : colour}
        if dat not in self.__data:
            raise Exception("Invalid data")
        for _, size in windows.items():
            data[f"SMA_{size}"] = data[dat].rolling(window=size).mean()
        for colour, size in windows.items():
            plt.plot(data[f"SMA_{size}"], label=f'{size}-Day SMA', color=colour)

    def show(self):
        plt.legend()
        plt.show()

graph = Display_Graph("Simple Moving Average (SMA)")
graph.add_SMA("Close",red=20,green=50)
graph.add_SMA("Close",orange=100)
graph.add_data("High")
graph.show()