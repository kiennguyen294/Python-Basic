from dataclasses import make_dataclass
from dataclasses import dataclass

Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)


class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low


stock_reg_class = StockRegClass("FB", 177, high=178, low=175)

@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float


def main():
    stock
    stock_reg_class


if __name__ == '__main__':
    main()
