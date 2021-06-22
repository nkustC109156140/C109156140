# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:03:23 2021

@author: User
"""
def main():
    m1={"1":72, "2":62, "3":82, "4":44,"5":60}
    ma={"A":55,"B":68}
    drink={"是":7,"否":0,}
    fries={"是":13,"否":0}
    money=0
    meal= (input("主餐和聲及套餐:")) 
    # list 把輸入的東西分開來
    money+=m1[meal[0]]
    money+=ma[meal[1]]   
    money+=drink[input("是否升級大悲:")]
    money+=fries[input("受否升級大暑:")]
    print("總共為",str(money),"元")
main()