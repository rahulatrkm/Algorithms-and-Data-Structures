# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 23:00:53 2018

@author: rahul

for coursera course
"""

def mul(x,y):
    if len(x) == 2:
        a = int(x[0])
        b = int(x[1])
        c = int(y[0])
        d = int(y[1])
        
        return ((100*a*c) + (10*(a*d + b*c)) + b*d)
    else:
        l = int(len(x)/2)
        ta = x[:l]
        tb = x[l:]
        tc = y[:l]
        td = y[l:]
        return (((10**(2*l))* mul(ta,tc)) + ((10**l)*(mul(ta,td) + mul(tb,tc))) + mul(tb,td))

a = input()
b = input()
if len(a) % 2 != 0:
    a = '0' + a
if len(b) % 2 != 0:
    b = '0' + b
# debugging the o/p of padded number
# print(a,b)
ans =  mul(a,b)
print(ans)