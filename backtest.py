from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import numpy as np
import pandas_ta as ta


print(GOOG)


def indicator(data):
    # data akan menjadi OHLCV
    return data.Close.s.pct_change(periods=7) * 100


class MomentumStrategy(Strategy):
    def init(self):
        self.pct_change = self.I(indicator, self.data)

    def next(self):
        change = self.pct_change[-1]

        if self.position:
            if change < 0:
                self.position.close()
        else:
            if change > 5 and self.pct_change[-2] > 5:
                self.buy()


bt = Backtest(GOOG, MomentumStrategy, cash=10_000)

stats = bt.run()
bt.plot()
print(stats)
