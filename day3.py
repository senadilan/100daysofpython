# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 13:32:30 2025

@author: sena
"""

""" 
Project 3
"""
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# İlk seçim
first_choice = input("Type 'left' or 'right': ").lower()

if first_choice == "left":
    # İkinci seçim
    second_choice = input("Do you want to 'swim' or 'wait'? ").lower()
    
    if second_choice == "wait":
        # Üçüncü seçim
        third_choice = input("Which door? Type 'red', 'blue', or 'yellow': ").lower()
        
        if third_choice == "yellow":
            print("You Win!")
        elif third_choice == "red":
            print("Burned by fire. Game Over.")
        elif third_choice == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

