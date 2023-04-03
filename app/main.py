from data import fetch
from frontier import Frontier
from portfolio import Portfolio

if __name__ == '__main__':
    data = fetch(["AAPL", "MSFT", "LLY", "PLTR", "GOOG"])
    tick=Portfolio(data)
    tick.compute()

    frontier = Frontier(tick)
    frontier.compute()