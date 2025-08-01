# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 16:31:45 2025

@author: sena
"""


def add(n1,n2):
    return n1+n2
def subtrack(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtrack,
    "*":multiply,
    "/":divide,
    }
    
def calculator():
    should_accumulate=True
    num1=input("enter the first number:")
    
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("pick the symbols:")    
        num2=input("enter the second number:")
        answer=operations[operation_symbol](num1,num2)
        print("{} {} {} ={}".format(num1,operation_symbol,num2,answer))
    
        choice=input(f"type 'y' to continue calculating with {answer},or type 'n' to start :")
    
        if choice=="y":
            num1=answer
        else:
           should_accumulate=False  
           print("\n"*20)    
           calculator()
           
calculator()           