# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:46:46 2020

@author: user
"""

#Chinese Remainder theorem
#a,b are coprimes
def extended_gcd(a,b):
    assert a>=0 and b>=0 and a+b>0
    if b==0:
        x,y=1,0
    else:
        p,q=extended_gcd(b,a%b)
        x=q
        y=p-q*(a//b)
    assert 1==a*x+b*y
    return (x,y)
def ChineseRemainder(a,ra,b,rb):
    x,y=extended_gcd(a,b)
    r=ra*b*y+rb*a*x
    m=a*b
    return ((r%m+m)%m)
