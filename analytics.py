import pandas as pd
import matplotlib.pyplot as plt
from fetch_api import get_info_stock

data = get_info_stock("GOOG")

def display_graph(**indicators):
    i = 0
    for indicator, w in indicators['dat'].items():
        data[indicator] = data['Close'].rolling(window=w).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    for indicator, w in indicators['dat'].items():
        plt.plot(data[indicator], label=f'{w}-Day {indicators["tag"]}', color=indicators["colours"][i])
        i += 1
    plt.title(indicators["title"])
    plt.legend()
    plt.show()

display_graph(title="Simple Moving Average (SMA)", dat={"SMA_20":20,"SMA_50":50}, colours=["red","green"], tag="SMA")

# TO-DO: More effective using a class and setting each method to a different indicator.