import numpy as np
import matplotlib.pyplot as plt

# Define the mean returns and covariance matrix of the assets
mean_returns = np.array([0.05, 0.1, 0.15])
covariance_matrix = np.array([[0.06, 0.02, 0.01],
                              [0.02, 0.07, 0.03],
                              [0.01, 0.03, 0.08]])

# Define a set of portfolio weights
portfolio_weights = np.array([0.4, 0.3, 0.3])

# Calculate the expected return and volatility of the portfolio
portfolio_return = np.dot(mean_returns, portfolio_weights)
portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(covariance_matrix, portfolio_weights)))

# Define a range of portfolio weights
num_portfolios = 100
portfolio_weights_range = np.linspace(0, 1, num_portfolios)

# Calculate the expected return and volatility of each portfolio
portfolio_returns = []
portfolio_volatilities = []
for w1 in portfolio_weights_range:
    for w2 in portfolio_weights_range:
        w3 = 1 - w1 - w2
        if w3 >= 0:
            portfolio_weights = np.array([w1, w2, w3])
            portfolio_return = np.dot(mean_returns, portfolio_weights)
            portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(covariance_matrix, portfolio_weights)))
            portfolio_returns.append(portfolio_return)
            portfolio_volatilities.append(portfolio_volatility)

# Plot the set of portfolio returns and volatilities
plt.figure(figsize=(8, 6))
plt.scatter(portfolio_volatilities, portfolio_returns, alpha=0.3)
plt.xlabel('Volatility')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')

# Choose a risk-free rate of return
risk_free_rate = 0.03

# Calculate the slope and intercept of the capital market line
covariance_vector = np.dot(covariance_matrix, portfolio_weights)
market_portfolio_return = np.dot(mean_returns, portfolio_weights)
market_portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(covariance_matrix, portfolio_weights)))
market_portfolio_sharpe_ratio = (market_portfolio_return - risk_free_rate) / market_portfolio_volatility
capital_market_line_slope = market_portfolio_sharpe_ratio
capital_market_line_intercept = risk_free_rate

# Plot the capital market line
plt.plot([0, market_portfolio_volatility], [risk_free_rate, market_portfolio_return], 'r-', label='Capital Market Line')
plt.legend()

plt.show()

