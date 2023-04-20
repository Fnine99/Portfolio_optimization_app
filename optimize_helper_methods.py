import numpy as np

class Helpers:
    def __init__(self, portfolio, rf_rate) -> None:
        self.portfolio = portfolio
        self.rf_rate = rf_rate
        
    def weight_constraint(self, weights):
        return np.sum(weights) - 1
    
    def min_portfolio_return(self, weights):
        return np.dot(np.array(list(self.portfolio.arith_mean_returns.values())), weights)
    
    def max_portfolio_return(self, weights):
        return -np.dot(np.array(list(self.portfolio.arith_mean_returns.values())), weights)
    
    def min_portfolio_volatility(self, weights):
        return np.dot(np.transpose(weights), np.dot(self.portfolio.covariance_matrix, weights))
 
    def max_portfolio_volatility(self, weights):
        return -np.dot(np.transpose(weights), np.dot(self.portfolio.covariance_matrix, weights))

    def max_sharpe_ratio(self, weights):
        return -((np.dot(np.array(list(self.portfolio.arith_mean_returns.values())), weights)-self.rf_rate)/
                np.sqrt(np.dot(np.transpose(weights), np.dot(self.portfolio.covariance_matrix, weights))))