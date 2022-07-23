# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:19:16 2022

@author: gati6
"""

N = int(input("How many stick (N) in the pile :"))
print("There are",N,"sticks in the pile.")
name = input("What is your name :")
time = 1
sum = N
while N > 0 :
    print(name,",",end="")
    S = int(input("How many sticks you will take(1-2) :"))
    if((S==1 or S==2)and(sum>=S)):
        sum = sum-S
        if(sum > 0):
            print("There are",sum,"sticks in the pile.")
            time = time+1
        elif(sum == 0):
            print("OK. There is no stick left in the pile.You spent",time,"times.")
            break
    elif((S==1 or S==2)and(sum<S)):
        print("There are no enough sticks to take.")
    elif(S>2):
        print("No you cannot take more than 2 sticks!")
    else:
        print("No you cannot take more less than 1 stick!")
        
world

