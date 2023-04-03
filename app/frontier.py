import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from optimize import Optimize

class Frontier(Optimize):
    def __init__(self, portfolio, iterations:int=1000000, bounds=[0.000, 0.900], rf_rate=0.045) -> None:
        super().__init__(portfolio, bounds, rf_rate)

        self.portfolios_returns=[]
        self.portfolios_stdev=[]
        self.portfolios_weights=[]

        self.number_of_assets = len(self.portfolio.portfolio_weights)

        self.portfolio_iterations = iterations
    
    def compute(self):
        for portfolio in range(self.portfolio_iterations):
            assets_weights = np.random.random(self.number_of_assets)
            assets_weights = assets_weights/np.sum(assets_weights)
            infos = self.get_portfolio_infos(assets_weights)
            self.portfolios_returns.append(infos[0])
            self.portfolios_stdev.append(infos[1])
            self.portfolios_weights.append(infos[2])
            

        data = {'Returns':self.portfolios_returns, 'Volatility':self.portfolios_stdev}

        for counter, symbol in enumerate(list(self.portfolio.arith_mean_returns.keys())):
            data[symbol+' weight'] = [w[counter] for w in self.portfolios_weights]

        portfolios = pd.DataFrame(data)
        test = pd.DataFrame(self.portfolio.monthly_returns, self.portfolio.dates[:self.portfolio.min_length-1])
        test.plot.line(alpha=0.3, grid=True, figsize=[10,8])
        plt.title("Monthly Returns")

        test1 = pd.DataFrame.from_dict(self.portfolio.arith_mean_returns, orient='index', columns=['Arithmetic Returns'])
        test2 = pd.DataFrame.from_dict(self.portfolio.geo_mean_returns, orient='index', columns=['Geometric Returns'])
        combined = pd.concat([test1, test2], axis=1)
        y = combined.plot(kind="bar", alpha=0.3, grid=True, figsize=[10,8])
        y.set_ylabel('Returns')
        plt.title("Average Returns")
        
        test3 = pd.DataFrame.from_dict(self.portfolio.stdev, orient='index', columns=['Standard Deviation'])
        y1 = test3.plot(kind="bar", alpha=0.3, grid=True, figsize=[10,8])
        y1.set_ylabel('Volatility')
        plt.title("Returns Volatility")

        min_vol_port = portfolios.iloc[portfolios['Volatility'].idxmin()]

        portfolios.plot.scatter(x='Volatility', y='Returns', marker='o', s=10, alpha=0.3, grid=True, figsize=[10,8])

        optimal_risky_port = portfolios.iloc[((portfolios['Returns']-self.rf_rate)/portfolios['Volatility']).idxmax()]

        optimized_min_vol_port = self.minimize_volatility()
        optimized_optimal_risky_port = self.optimal_portfolio()
        plt.scatter(optimized_min_vol_port[1], optimized_min_vol_port[0], color='g', marker='o', s=15, label="Optimized minimum volatility portfolio")
        plt.scatter(optimized_optimal_risky_port[1], optimized_optimal_risky_port[0], color='g', marker='+', s=20, label="Optimized maximum Sharpe ratio portfolio")
        plt.scatter(min_vol_port[1], min_vol_port[0], color='r', marker='o', s=15, label="Located minimum volatility portfolio")
        plt.scatter(optimal_risky_port[1], optimal_risky_port[0], color='r', marker='+', s=20, label="Located maximum Sharpe ratio portfolio")

        plt.title(f"Efficient Frontier [{self.portfolio_iterations} portfolios modeled]")
        plt.legend()
        plt.show()