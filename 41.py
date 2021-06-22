# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 14:50:15 2021

@author: c109156119
"""

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = [int((-b + (b**2 - 4*a*c)**0.5) / 2*a), int((-b - (b**2 - 4*a*c)**0.5) / 2*a)]
    if sum(x) == 0: print(0)
    else:
        if 0 in x: x.remove(0)
        print(x)
        
main()
