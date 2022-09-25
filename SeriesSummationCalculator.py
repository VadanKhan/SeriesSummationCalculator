# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:17:14 2022

@author: Nicholas
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100)
print(x)

#creating the natural number range in n
N = 100
n = np.arange(1,N+1) 
print(n)

yvals = np.array([])
sumvals = np.array([])

a_0 = np.pi/2
print(a_0)

for k in x:
    for h in n:
        sumval = (2/((np.pi)*h**2))*(np.cos(h*np.pi)-1)*np.cos(h*k)
        sumvals = np.append(sumval, sumvals)
    print(sumvals)
    sumt = sum(sumvals)
    print(sumt)
    y = sumt + a_0
    yvals = np.append(yvals, y)
    sumvals = []

print(yvals)

plt.plot(x,yvals,label='fourier series')
plt.legend()
plt.show()


