# src/visualizer.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_top_traded(data, n=10):
    df = pd.DataFrame(data)
    top = df['Ticker'].value_counts().head(n)
    top.plot(kind='bar', title="Top Traded Stocks by Politicians")
    plt.tight_layout()
    plt.show()
