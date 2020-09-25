#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:35:06 2020

@author: rajatdua
"""
"""
In this problem, BSImpVol.py, I have defined a function bsimpvol which returns the implied 
volatility using Black Scholes Formula, bsformula. It uses iterative methods of newton or 
bisection to compute the Implied Volatility. I have used partial function to pass the input 
variables in the bsformula to find option value and vega as a function of sigma, that is, 
volatility. For both the methods, I have used the difference between optionValue and price 
as the function variable. For the newton method, I have used vega as the derivative function. 
I validated the output using the online implied volatility calculator. I have tested the code 
by incorporating all the necessary conditions that were mentioned in the problem.

After comparing the convergence properties of Newton’s method against the bisection method, 
I conclude that Newton Method does a far better job in computing the implied volatility as 
compared to the bisection method since the number of iterations required for the newton’s 
method is far less than the bisection method. For out of the money (OTM) European option, 
the performance difference between newton and bisect method is more noticeable.   
"""

# In[193]:

from BS import bsformula
from Bisect import newton
from Bisect import bisect
from functools import partial

# In[194]:

def bsimpvol( callput, S0, K, r, T, price, q=0., priceTolerance=0.01, method='bisect' , reportCalls=False ):
    
    if price != 'NaN' and price >=callput*(S0 - K):
        def bsmvsact(sigma, callput, S0, K, r, T, price):
            
            return bsformula(callput, S0, K, r, T, sigma, q=0.)[0] - price
        
        def vega(sigma, callput, S0, K, r, T):
            
            return bsformula(callput, S0, K, r, T, sigma, q=0.)[2]
            
        partial_bsmvsact = partial(bsmvsact, callput = callput, S0 = S0, K = K, r = r, T = T, price = price)
        partial_vega = partial(vega, callput = callput, S0 = S0, K = K, r = r, T = T )
                
        if method =='bisect':    
            root, diff, iterations = bisect(0, partial_bsmvsact, None, [0, 2], [0.00001, 0.0001], 1000)
            n_calls = iterations            
            
        elif method == 'newton':
            root, diff, iterations = newton(0, partial_bsmvsact, partial_vega, 1.0, 0, [0.00001, 0.0001], 1000)
            n_calls = 2*iterations
               
        if root:
            if reportCalls: return root[-1], n_calls
            else: return root[-1]
        else: 
            if reportCalls: return 'NaN', n_calls
            else: return 'NaN'
        
    else: return 'NaN'

# In[195]:

print(bsimpvol(1, 95., 100., 0.05, 1.0, 10., 0., 0.0001, 'newton', True ))

