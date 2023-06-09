import numpy as np
import pandas as pd

from assets import Assets

class Portfolio(Assets):
    """ This class will model a portfolio object"""
    def __init__(self, data) -> None:
        super().__init__(data)

#---------------------------- portfolio information methods --------------------------#
    def cpt_portfolio_return(self):
        self.portfolio_return = np.dot(np.array(list(self.arith_mean_returns.values())), self.portfolio_weights)

    def cpt_covariance_matrix(self):
        self.covariance_matrix = np.cov(np.array(list(self.monthly_returns.values())))
    
    def cpt_portfolio_variance(self):
        self.portfolio_variance = np.dot(np.transpose(self.portfolio_weights), np.dot(self.covariance_matrix, self.portfolio_weights))

    def cpt_portfolio_stdev(self):
        self.portfolio_stdev = np.sqrt(self.portfolio_variance)

    def cpt_correlation_matrix(self):
        self.correlation_matrix = np.corrcoef(np.array(list(self.monthly_returns.values())))
    
    def cpt_inverse_covariance_matrix(self):
        """ Mcov^(-1) """
        self.inverse_covariance_matrix = np.linalg.inv(self.covariance_matrix)

    def compute(self):
        """ puplic method that will be called to calculate the statistics of the given porfolio """
        self.get_monthly_prices()
        self.cpt_monthly_returns()
        self.cpt_arith_mean_return()
        self.cpt_geo_mean_return()
        self.cpt_std_deviation()
        self.cpt_portfolio_return()
        self.cpt_covariance_matrix()
        self.cpt_portfolio_variance()
        self.cpt_portfolio_stdev()
        self.cpt_correlation_matrix()
        self.cpt_inverse_covariance_matrix()
