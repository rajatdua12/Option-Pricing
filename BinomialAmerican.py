#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:51:08 2020

@author: rajatdua
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:03:59 2019

@author: rajatdua
"""
"""
In this problem, BinomialAmerican.py, I have defined a function binomialAmerican to find the 
value of American options with input values spot price (S0), strike price (Ks), yield to maturity (r), 
Time to Maturity (T) (in years), volatility (sigma), dividend yield rate (q), callputs to determine 
whether the option is Call or put, and the number of timesteps in binomial tree (M). I have used these 
input variables to extract a tuple of 2 values, that is, payoff of the option at timestep t = 0 
(option value now) and also the difference between option value calculated from black-scholes 
formula and binomial tree as price error. I have compared the final value with the output generated 
bsformula for the option value and found out that the final value from binomialAmerican is very close 
to the output generated by the bsformula. I created a plot comparing the variation of price Error between 
bsformula and binomialAmerican with Number of timesteps(M).

This chart clearly shows that the price error decreases drastically with increase in the number of 
timesteps.
"""

from BS import bsformula
import numpy as np
import matplotlib.pyplot as plt

def binomialAmerican(S0, Ks, r, T, sigma, q, callputs, M):

    """ Computed values """
    
    dt = T/M  # Single time step, in years
    df = np.exp(-(r-q) * dt)  # Discount factor

    u = np.exp(sigma*np.sqrt(dt))
    d = 1./u
    p = (np.exp((r-q)*dt) - d)/(u - d)
    q = 1-p

    # Initialize a 2D tree at T=0
    STs = [np.array([S0])]
    
    # Simulate the possible stock prices path
    for i in range(M):
        prev_branches = STs[-1]
        st = np.concatenate((prev_branches*u,
                             [prev_branches[-1]*d]))
        STs.append(st)  # Add nodes at each time step

    payoffs = np.maximum(0, (STs[M]-Ks) if callputs==1 else (Ks-STs[M]))
        
        
    for j in reversed(range(M)):
        # The payoffs from NOT exercising the option
        payoffs = (payoffs[:-1] * p + payoffs[1:] * q) * df
        early_ex_payoff = (STs[j] - Ks) if callputs==1 else (Ks - STs[j])
        payoffs = np.maximum(payoffs, early_ex_payoff)

    price = bsformula(callput = callputs, S0 = S0, K = Ks, r = r, T = T, sigma = sigma, q = q)[0]
    error = price - payoffs[0]
    
    return payoffs[0], error
    
if __name__ == '__main__':
    
    print(binomialAmerican(50., 50., 0.05, 0.5, 0.3, 0., 1, 600))
    
    M = np.delete(np.linspace(0, 1000, 101), 0)
    
    Y = [binomialAmerican(50., 50., 0.05, 0.5, 0.3, 0., 1, int(m))[1] for m in M]
    
    
    X = M

    plt.figure(1)
    plt.plot(X, Y, 'r')
    plt.title('Price Error Vs Number of Timesteps')
    plt.xlabel('Number of Timesteps')
    plt.ylabel('Price Error')
    
    
    