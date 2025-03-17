# European Option Pricing with the B&S Model

import numpy as np
import scipy.stats as ss

def BlackScholes(S,K,T,r,Sigma,Option_Type) :
    d1 = (np.log(S/K)+(r+0.5*((Sigma)**(2)))*T)/(Sigma*np.sqrt(T))
    d2 = d1 - Sigma*np.sqrt(T)
    if Option_Type == 'Call':
        Price= S*ss.norm.cdf(d1)-K*(np.exp(-r*T))*ss.norm.cdf(d2)
    elif Option_Type == 'Put':
        Price= K*(np.exp(-r*T))*ss.norm.cdf(-d2)-S*ss.norm.cdf(d1)
    return Price
    
# For testing
S = 90 # Current Underlying Price
K = 100 # Strike
T = 1 # Time to Maturity (in Years)
r = 0.02 # Risk-Free Rate
Sigma = 0.25 # Volatility
Option_Type = 'Call' # Option Type

P = BlackScholes(S, K, T, r, Sigma, Option_Type)
print(f'The price of the {Option_Type} is: {P:.2f}')


# Simulating a stock price possible movements (MonteCarlo)

import matplotlib.pyplot as plt

def simulate_stocks_paths(S0,Sigma,T,N):
    Number_of_Trading_Days = 252
    dt = T/Number_of_Trading_Days
    Prices_Matrix = np.zeros((Number_of_Trading_Days+1,N))
    Prices_Matrix[0]=S0
    for i in range(1,Number_of_Trading_Days+1):
        Norm = np.random.normal(0,1,N)
        Prices_Matrix[i]=Prices_Matrix[i-1]*(1+Sigma*Norm*np.sqrt(dt))
    return Prices_Matrix
        

#For testing
S0 = 100
Sigma = 0.2
T = 1
N = 100

Simulation = simulate_stocks_paths(S0, Sigma, T, N)
for i in range(N):
    plt.plot(Simulation[:,i])
plt.title('Simulation Prix Stocks')
plt.xlabel('Days')
plt.ylabel('Price')
plt.show()