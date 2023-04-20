import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from optimize import Optimize

class Frontier(Optimize):
    def __init__(self, portfolio, iterations:int=20000, bounds=[0.000, 0.900], rf_rate=0.045) -> None:
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
        
        portfolios_data = {'Returns':self.portfolios_returns, 'Volatility':self.portfolios_stdev}
        
        for counter, symbol in enumerate(list(self.portfolio.arith_mean_returns.keys())):
            portfolios_data[symbol+' weight'] = [w[counter] for w in self.portfolios_weights]
        
        self.portfolios = pd.DataFrame(portfolios_data)

        self.portfolios.plot.scatter(x='Volatility', y='Returns', marker='o', s=10, alpha=0.3, grid=True, figsize=[10,8])

        self.max_return = self.portfolios.iloc[self.portfolios['Returns'].idxmax()]
        self.min_vol_port = self.portfolios.iloc[self.portfolios['Volatility'].idxmin()]
        self.optimal_risky_port = self.portfolios.iloc[((self.portfolios['Returns']-self.rf_rate)/self.portfolios['Volatility']).idxmax()]
        
        self.optimized_max_return_port = self.maximize_return()
        self.optimized_min_vol_port = self.minimize_volatility()
        self.optimized_optimal_risky_port = self.optimal_portfolio()