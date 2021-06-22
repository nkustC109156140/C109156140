# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 12:32:13 2021

@author: c109156119
"""
def main():
    ans=list(map(int,list(input("請輸入第一組數字"))))
    ram=list(map(int,list(input("請輸入第二組數字"))))
    a,b=0,0
    for i in range(len(ram)):
        if ram[i]== ans[i]:a+=1
        elif ram[i] in ans:b+=1
    if a ==len(ram):print(a,"A",b,"B","全對")
main()
    