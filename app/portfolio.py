from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

class Portfolio:
    """ This class will model a portfolio object"""
    def __init__(self, data) -> None: #send in one batch or muktiple batches? 
        self.data=data
        self.monthly_prices={}
        self.monthly_returns={}
        self.arith_mean_returns={}
        self.geo_mean_returns={}
        self.std_deviation={}


        self.risk_free_rate=0.03
        self.portfolio_weights=np.array([1/len(self.data) for i in self.data]) # 1 stock exep.

#---------------------------- security information methods --------------------------#  
    def get_monthly_prices(self):
        """ 2 scenarios: 
            -when the class receive multiple stock infos, the data shape will be as follows;
            {
                'aapl':{'meta': {'symbol': 'aapl', 'interval': '1month', ...}, values: [{'open': '100', 'close': '101', ...}, {...}, ...], 'status': 'ok'},
                'goog':{'meta': {'symbol': 'goog', 'interval': '1month', ...}, values: [{'open': '100', 'close': '101', ...}, {...}, ...], 'status': 'ok'}
            }
                >loop through the keys ... aapl, goog
                >init. object in monthly_prices with the key
                >loop through the values of each data[symbol] and retreive the float(value['closing price'])
            -rare scenario of only one stock info...
        """
        for symbol in self.data.keys():
            self.monthly_prices[symbol] = np.array([float(value["close"]) for value in self.data[symbol]["values"]])
    
    def cpt_monthly_returns(self):
        """
            loop through the monthly_prices and add the each return((price[t+1]/price[t])-1) to monthly_returns
            *note: you could do this; np.array([(self.monthly_prices[symbol][index+1]/price)-1 for price, index in enumerate(self.monthly_prices[symbol])]) 
            but dealing with the index out of bound becomes much harder
        """
        for symbol in self.monthly_prices.keys():
            self.monthly_returns[symbol] = np.array([(self.monthly_prices[symbol][i+1]/self.monthly_prices[symbol][i])-1 for i in range(len(self.monthly_prices[symbol])-1)])
    
    def cpt_arith_mean_return(self) -> float:
        """
            arithmetic mean of each monthly returns array rounded to 2 decimals
        """
        for symbol in self.monthly_returns.keys():
            self.arith_mean_returns[symbol] = round(np.mean(self.monthly_returns[symbol]), 2)

    def cpt_geo_mean_return(self) -> float:
        """
            geo mean of each monthly returns array rounded to 2 decimals
            >new array of 1 + each monthly return
            >the product of the elements of that new array
            >that product elevated to power of 1/len(monthly returns array)
            > -1
            *note: or just from scipy.stats import gmean ... 
        """
        for symbol in self.monthly_returns.keys():
            self.geo_mean_returns[symbol] = round(np.power(np.prod([1+r for r in self.monthly_returns[symbol]]), 1/len(self.monthly_returns[symbol]))-1, 2)
    
    def cpt_std_deviation(self) -> float:
        """
            standard deviation of each monthly returns array rounded to 2 decimals
        """
        for symbol in self.monthly_prices.keys():
            self.std_deviation[symbol] = round(np.std(self.monthly_returns[symbol]), 2)
    
#---------------------------- portfolio information methods --------------------------#
    def cpt_portolio_return(self): #**** fix
        self.portfolio_return = np.dot(np.array(list(self.arith_mean_returns.values())), self.portfolio_weights)
    
    
    def cpt_portfolio_var(self):
        self.portfolio_var = np.dot(np.transpose(self.portfolio_weights), np.dot(self.cpt_covar_matrix(), self.portfolio_weights))
    
    def cpt_portfolio_std(self):
        return np.sqrt(self.portfolio_var)

    def cpt_covar_matrix(self): #******
        self.covariance_matrix = np.cov(np.array(list(self.monthly_returns.values())))
        print(self.covariance_matrix)

    def cpt_correlation_matrix(self): #*****
        data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        correlation_matrix = np.corrcoef(data)
        print(correlation_matrix)
    
    def cpt_inv_covar_matrix(self): #*****
        """ Mcov^(-1) """
        return np.linalg.inv(self.cpt_covar_matrix())

#---------------------------- portfolio optimization methods --------------------------#
    def cpt_portfolios(self):
        mean_returns = np.array([0.05, 0.1, 0.15])
        covariance_matrix = np.array([[0.06, 0.02, 0.01],
                              [0.02, 0.07, 0.03],
                              [0.01, 0.03, 0.08]])
        portfolio_weights = np.array([0.4, 0.3, 0.3])

        self.portfolios_returns=[]
        self.portfolios_std=[]
        iterator=100
        portfolio_weights_range=np.linspace(0, 1, iterator)

        for w1 in portfolio_weights_range:
            for w2 in portfolio_weights_range:
                w3 = 1 - w1 - w2
                if w3 >= 0:
                    portfolio_weights = np.array([w1, w2, w3])
                    portfolio_return = np.dot(mean_returns, portfolio_weights)
                    portfolio_volatility = np.sqrt(np.dot(np.transpose(portfolio_weights), np.dot(covariance_matrix, portfolio_weights)))
                    self.portfolios_returns.append(portfolio_return)
                    self.portfolios_std.append(portfolio_volatility)

#---------------------------- visualization --------------------------#
    def viz_CML(self, show=False):
        self.cpt_portfolios()
        plt.figure(figsize=(8, 6))
        plt.scatter(self.portfolios_std, self.portfolios_returns, alpha=0.3)
        plt.xlabel('Volatility')
        plt.ylabel('Expected Return')
        plt.title('Efficient Frontier')
        
        plt.plot([0, self.portfolios_std], [self.risk_free_rate, self.portfolios_returns], 'r-', label='Capital Market Line')
        plt.legend()
        if show: return plt.show()

    def viz_SML(self, show=False):
        # fix
        # self.cpt_portfolios()
        plt.plot([0, self.portfolios_std], [self.risk_free_rate, self.portfolios_returns], 'r-', label='Capital Market Line')
        plt.legend()
        if show: return plt.show()

    def show(self):
        self.cpt_portfolios()
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
    tick.cpt_correlation_matrix()
    tick.viz_SML(True)
    