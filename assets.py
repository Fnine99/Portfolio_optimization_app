import numpy as np

class Assets:
    def __init__(self, data) -> None:
        self.data=data
        
        self.min_length = min([len(data["values"]) for data in self.data.values()])    ## temporary method
        for data in self.data.values():
            data["values"] = data['values'][:self.min_length]

        self.monthly_prices={}
        self.monthly_returns={}
        self.arith_mean_returns={}
        self.geo_mean_returns={}
        self.stdev={}

        self.tickers = np.array(list(self.data.keys()))
        self.dates = np.array([data["datetime"] for data in list(self.data.values())[0]["values"]])
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
            self.monthly_returns[symbol] = np.array([round((self.monthly_prices[symbol][t+1]/self.monthly_prices[symbol][t])-1, 4) for t in range(len(self.monthly_prices[symbol])-1)])
    
    def cpt_arith_mean_return(self) -> float:
        """
            arithmetic mean of each monthly returns array rounded to 2 decimals
        """
        
        for symbol in self.monthly_returns.keys():
            self.arith_mean_returns[symbol] = round(np.mean(self.monthly_returns[symbol]), 4)

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
            self.geo_mean_returns[symbol] = round(np.power(np.prod([1+r for r in self.monthly_returns[symbol]]), 1/len(self.monthly_returns[symbol]))-1, 4)
    
    def cpt_std_deviation(self) -> float:
        """
            standard deviation of each monthly returns array rounded to 2 decimals
        """
        for symbol in self.monthly_prices.keys():
            self.stdev[symbol] = round(np.std(self.monthly_returns[symbol]), 4)