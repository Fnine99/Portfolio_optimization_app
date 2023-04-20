import numpy as np
from scipy.optimize import minimize

from optimize_helper_methods import Helpers

class Optimize:
    def __init__(self, portfolio, bounds, rf_rate) -> None:
        self.portfolio=portfolio
        self.rf_rate=rf_rate
        self.bounds = [(bounds[0],bounds[1]) for i in range(len(self.portfolio.portfolio_weights))]
        self.helper_fn = Helpers(portfolio, self.rf_rate)
    # ------------------- infos method ----------------- #
    def get_portfolio_infos(self, weights) -> tuple:
        """
            Calculate a given portfolio infomations
            
            Args:
            weights (np.array): The assets weights
            
            Returns:
            returns, standard deviation and weights of assets of the portfolio
        """
        returns = np.dot(np.array(list(self.portfolio.arith_mean_returns.values())), weights)
        variance = np.dot(np.transpose(weights), np.dot(self.portfolio.covariance_matrix, weights))
        stdev = np.sqrt(variance)
        return returns, stdev, weights
    
    # ------------------- optimization methods ----------------- #
    def minimize_return(self):
        constraints={'type':'eq', 'fun':self.helper_fn.weight_constraint}
        result = minimize(self.helper_fn.min_portfolio_return, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def maximize_return(self):
        constraints={'type':'eq', 'fun':self.helper_fn.weight_constraint}
        result = minimize(self.helper_fn.max_portfolio_return, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def minimize_volatility(self):
        constraints={'type':'eq', 'fun':self.helper_fn.weight_constraint}
        result = minimize(self.helper_fn.min_portfolio_volatility, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def maximize_volatility(self):
        constraints={'type':'eq', 'fun':self.helper_fn.weight_constraint}
        result = minimize(self.helper_fn.max_portfolio_volatility, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)

    def optimal_portfolio(self):
        constraints={'type':'eq', 'fun':self.helper_fn.weight_constraint}
        result = minimize(self.helper_fn.max_sharpe_ratio, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
