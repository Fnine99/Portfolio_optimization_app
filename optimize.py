import numpy as np
from scipy.optimize import minimize

class Optimize:
    def __init__(self, portfolio, bounds, rf_rate) -> None:
        self.portfolio=portfolio
        self.rf_rate=rf_rate
        self.bounds = [(bounds[0],bounds[1]) for i in range(len(self.portfolio.portfolio_weights))]
    
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

    # ------------------- lambdas ----------------- #
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
    
    # ------------------- optimization methods ----------------- #
    def minimize_return(self):
        constraints={'type':'eq', 'fun':self.weight_constraint}
        result = minimize(self.min_portfolio_return, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def maximize_return(self):
        constraints={'type':'eq', 'fun':self.weight_constraint}
        result = minimize(self.max_portfolio_return, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def minimize_volatility(self):
        constraints={'type':'eq', 'fun':self.weight_constraint}
        result = minimize(self.min_portfolio_volatility, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
    
    def maximize_volatility(self):
        constraints={'type':'eq', 'fun':self.weight_constraint}
        result = minimize(self.max_portfolio_volatility, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)

    def optimal_portfolio(self):
        constraints={'type':'eq', 'fun':self.weight_constraint}
        result = minimize(self.max_sharpe_ratio, self.portfolio.portfolio_weights, method='SLSQP', bounds=self.bounds, constraints=constraints)
        return self.get_portfolio_infos(result.x)
               