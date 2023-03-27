from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

class Portfolio:
    """ This class will model a portfolio object"""
    def __init__(self, data) -> None: #send in one batch or muktiple batches? 
        self.data=data
        self.risk_free_rate=0.03
        self.portfolio_weights=np.array([1/len(self.data["values"]) for i in range(len(self.data["values"]))])

#---------------------------- security information methods --------------------------#  
    def get_monthly_prices(self) -> list:
        """ each daloops  """
        values=self.data['values']
        return np.array([float(price['close']) for price in values])
    
    def cpt_monthly_returns(self):
        prices=self.get_monthly_prices()
        return np.array([(prices[i+1]/prices[i])-1 for i in range(len(prices)-1)])
    
    def cpt_arith_mean_return(self) -> float:
        return round(np.mean(self.cpt_monthly_returns()), 2)

    def cpt_geo_mean_return(self) -> float:
        return round(np.exp(np.mean(np.log(self.cpt_monthly_returns()))), 2)
    
    def cpt_std_deviation(self) -> float:
        return round(np.std(self.cpt_monthly_returns()), 2)
    
#---------------------------- portfolio information methods --------------------------#
    def cpt_portolio_return(self): #**** fix
        return np.dot(self.cpt_monthly_returns(), self.portfolio_weights)
    
    def cpt_portfolio_var(self):
        return np.dot(np.transpose(self.portfolio_weights), np.dot(self.cpt_covar_matrix(), self.portfolio_weights))
    
    def cpt_portfolio_std(self):
        return np.sqrt(self.cpt_portfolio_var())

    def cpt_covar_matrix(self): #******
        data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        covariance_matrix = np.cov(data)
        print(covariance_matrix)

    def cpt_correlation_matrix(self): #*****
        """ Ra,b=cov(a,b)/𝜎(a)*𝜎(b) """
        corr = covar/std(a)*std(b)
    
    def cpt_inv_covar_matrix(self): #*****
        """ Mcov^(-1) """
        return np.linalg.inv(self.cpt_covar_matrix())

#---------------------------- portfolio optimization methods --------------------------#
    def cpt_portfolios(self):
        self.portfolios_returns=[]
        self.portfolios_std=[]
        iterator=100
        portfolio_weights_range=np.linspace(0, 1, iterator)

        for w1 in portfolio_weights_range:
            for w2 in portfolio_weights_range:
                w3 = 1 - w1 - w2
                if w3 >= 0:
                    portfolio_weights = np.array([w1, w2, w3])
                    portfolio_return = np.dot(self.cpt_portolio_return(), portfolio_weights)
                    portfolio_volatility = np.sqrt(np.dot(np.transpose(portfolio_weights), np.dot(self.cpt_covar_matrix(), portfolio_weights)))
                    self.portfolios_returns.append(portfolio_return)
                    self.portfolios_std.append(portfolio_volatility)

#---------------------------- visualization --------------------------#
    def viz_CML(self, show:bool):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.portfolios_std, self.portfolios_returns, alpha=0.3)
        plt.xlabel('Volatility')
        plt.ylabel('Expected Return')
        plt.title('Efficient Frontier')
        if show: return plt.show()

    def viz_SML(self, show:bool):
        # fix
        plt.plot([0, self.portfolios_std], [self.risk_free_rate, self.portfolios_returns], 'r-', label='Capital Market Line')
        plt.legend()
        if show: return plt.show()

    def show(self):
        self.viz_CML()
        self.viz_CML()
        plt.show()
#---------
    
    # def add(self, ticker, weight) -> None:
    #     self.tickers.append(ticker)
    #     self.stats.append(self.__calculate(ticker))
    
    # def __calculate(self, ticker) -> None:
    #     """ private method that will automaticaly calculate statistics for a given ticker """
    #     return 0
    
    # def calculate(self) -> None:
    #     """ puplic method that will be called to calculate the statistics of the given porfolio """
    #     return 0

    

if __name__ == '__main__':
    data_shape = {'meta': {'symbol': 'AAPL', 'interval': '1month', 'currency': 'USD', 'exchange_timezone': 'America/New_York', 'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'type': 'Common Stock'}, 'values': [{'datetime': '2023-03-01', 'open': '146.83000', 'high': '162.14000', 'low': '143.89999', 'close': '160.25000', 'volume': '1242101439'}, {'datetime': '2023-02-01', 'open': '143.97000', 'high': '157.38000', 'low': '141.32001', 'close': '147.41000', 'volume': '1286776720'}, {'datetime': '2023-01-01', 'open': '130.28000', 'high': '147.23000', 'low': '124.17000', 'close': '144.28999', 'volume': '1434399420'}], 'status': 'ok'}
    # x=data_shape['values']
    # print(x)
    tick=Portfolio(data_shape)
    tick.show()
    # print(x)
    