# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 13:32:30 2025

@author: sena
"""

""" Project2
Welcome to the tip calculator
What was the totAl bill?
How much tip would like to give?10,12 or 15?
How many people to split the bill?
Each person should pay:
"""
print("Welcome to the tip calculator\n")
total_bill=float(input("What was the totAl bill?:\n"))
tip=int(input("How much tip would like to give?10,12 or 15?:\n"))
people=int(input("How many people to split the bill?:\n"))
result=((total_bill*(tip*0.01))+total_bill)/people
print("Each person should pay:{}".format(result))
    
    

