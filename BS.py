#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:27:07 2020

@author: rajatdua
"""

#!/usr/bin/env python
# coding: utf-8

"""
In this problem, BS.py, I defined a function bsformula with input values callput [-1, 1], 
Spot Price (S0), Strike Price (K), interest rate (r), Time to maturity (T) (in years), volatility (sigma), 
and continuous dividend rate or foreign interest rate (q). I have used these inputs to compute the values 
of the Option Price, its delta and its vega. The function bsformula returns a 3-tuple optionValue, delta 
and vega. 
"""

import numpy as np
from scipy import stats

def bsformula(callput, S0, K, r, T, sigma, q=0):
    
    d_1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T)/(sigma*np.sqrt(T))
    
    d_2 = d_1 - sigma*np.sqrt(T)
    
    optionValue = callput*S0*stats.norm.cdf(callput * d_1) - callput*K*np.exp(-r*T)*stats.norm.cdf(callput*d_2)
    
    delta = callput*stats.norm.cdf(callput*d_1)
    
    vega = S0 * np.sqrt(T)*stats.norm.pdf(d_1)
    
    return optionValue, delta, vega

if __name__ == '__main__':
    print(bsformula(1, 100., 105., 0.05, 1.0, 0.2, 0.0 ))





