#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:38:52 2020

@author: rajatdua
"""
"""
In this problem, Bisect.py, I have defined 2 functions newton and bisect which are iterative methods to find the roots of the given function. For newton method, I have provided a security wherein if the start value is zero, then it will ask the user to enter the value of lower bound and upper bound. The iteration process will then start from the mid-point of upper and lower bound. In addition, if the average causes the derivative function to come out to be zero, I have incorporated another security wherein it will add some small random uniform variable between 0 and 0.01 to the derivative function in order to begin the iteration process. I have defined a list, xval, which captures all the values of iterative roots until the function root is captured, or the value of x comes within acceptable tolerance limit, defined by the tolerance input variable. Fdiff captures list of difference between each function output of each newton iteration and target value (generally, zero) until the function comes with in given tolerance input level.
For bisect method, I have provided security that if start value is None, then the function will start iteration from the mid-point of upper and lower bound.
"""

import random
import numpy as np

def newton(target, function, derivfun, start, bounds=None, tols=[0.001,0.010], maxiter=1000):
    """
            :param target: The target value of the function
            :param function: The function to solve
            :param derivfun: The derivative function of f
            :param start: Initial guess value of x
            :param bounds: upper and lower bound beyond which x shall not exceed.
            :param tols: the stopping criteria, the distance between successive x-values that indicates 
                        success and the difference between target and the y-value that indicates success.
            :param maxiter: Maximum number of iterations
            :return: The set of xvals tried by solver of the root (xvals(1) is the same as start),
                        the set of target − y values at the xvals (fdiffs)
    """
    n=1
    if start == 0.0:
        a = input('Enter the value of lower bound: ')
        b = input('Enter the value of upper bound: ')
        x=(int(a)+int(b))*0.5
    else:

        x = start
    
    xval = []
    fdiff = []
    
    while n<=maxiter:
        
        delta_y = derivfun(x)
        while delta_y == 0:
            delta_y = delta_y + np.random.uniform(0,1)*0.01
            
        x1 = x - function(x)/delta_y
        diff = target - function(x)
        
        xval.append(x)
        fdiff.append(diff)
        
        if abs(x1 - x) < tols[0] and abs(diff) < tols[1]:
            return xval, fdiff, n
        else:
            x = x1
            n += 1
            
    return None, None, n

def bisect(target, function, start=None, bounds=None, tols=[0.001,0.010], maxiter=1000):
    """
            :param target is the target value for the function f
            :param function is the handle for the function f.
            :param start is the x-value to start looking at. If None, the mean of the upper and lower bounds 
                shall be used. Subsequent steps shall always use the mean of the active bounds.
                This input is used  only when the initial bounds have not been supplied.
            :param bound is the upper and lower bound beyond which x shall not exceed.
            :param tols are the stopping criteria, the distance between successive x-values that indicates success 
                and the difference between target and the y-value that indicates success.
            :param maxiter is the maximum iteration count the solver shall note exceed.
    """
    
    xval = []
    fdiff = []
    
    if start != None:
        c=start
        
    elif start == None:
        if bounds != None:
            a = bounds[0] #input('Enter the value of lower bound: ')
            b = bounds[1] #input('Enter the value of upper bound: ')
            
            c=(a+b)*0.5
            
            n=1
            while n<=maxiter:
                
                c=(a+b)*0.5
                diff = target - function(c)
        
                xval.append(c)
                fdiff.append(diff)
        
                if diff == 0 or diff < tols[1] and abs(a - b)*0.5 < tols[0]:
                    return xval, fdiff, n
                else:
                    n += 1
                    
                if diff > 0:
                    a=c
                else:
                    b=c

            return c, None, n
        
if __name__ == '__main__':

    y = lambda x: x**3 + 2*x**2 - 5
    broot, bdiff, biterations = bisect(0, y, None, [0,2], [0.00001, 0.0001], 1000)
    print('\nBisection List Output:')
    print ('Roots list:', broot)
    print ('Difference from target list:', bdiff)
    
    print('\nBisection Final Output:')
    print ('Root is:', broot[-1])
    print ('Difference from target is:', bdiff[-1])
    print ('Total number of Iterations is:', biterations)


    y = lambda x: x**3 + 2*x**2 - 5
    dy = lambda x: 3*x**2 + 4*x
    nroot, ndiff, niterations = newton(0.0, y, dy, 1.0, 0, [0.00001, 0.0001], 1000)
    print('\nNewton List Output:')
    print ('Roots List:',nroot)
    print ('Difference from target list:', ndiff)
    
    print('\nNewton Final Output:')
    print ('Root is:', nroot[-1])
    print ('Difference from target is:', ndiff[-1])
    print ('Total number of Iterations is:', niterations)



