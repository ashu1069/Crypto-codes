# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:03:28 2020

@author: user
"""

#Modular Exponentiation
#for b^e(mod m),if e=2^k
def FastModularExponentiation1(b,k,m):
    b%=m
    for _ in range(k):
        b=b**2%m          #results b^(2^k)mod m
    return b
#For arbitrary e,convert the e into binary expression and then find b^(2^i)
#and multiply it for all e(i)=1
def FastModularExponentiation2(b,e,m):
#Code to convert numeric into binary,however python has an inbuilt function for it
    def binary(a):
        if a>1:
            binary(a//2)
        print (a%2,end='')   #prints as a string
    A=[int(i) for i in list('{0:0b}'.format(e))] #converts string into list
    r=1
    for i in range(len(A)-1,-1,-1):
        r=(r*b**int(A[i]))%m
        b=(b**2)%m
    return r
        
        