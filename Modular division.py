# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:26:08 2020

@author: user
"""

#Modular division
def extended_gcd(a,n):
    assert a>=0 and n>=0 and a+n>0
    if n==0:
        t,s=0,1
    else:
        p,q=extended_gcd(n,a%n)
        s=q
        t=p-q*(a//n)
    assert 1==a*s+n*t
    return (s,t)
def modular_div(a,b,n):
    s,t=extended_gcd(a,n)
    c=b*s
    return(c-n*(c//n))
