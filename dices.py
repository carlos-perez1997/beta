'''
description:
get player name
generate two random number into 2 dices
Dice 1: 1-6
Dice 2: 1-6
print dices values 
'''
import os
from random import randint

#funtions ##################
def get_dices():
    os.system('clear ')
    print("welcome to my parchis :::")

    #print("player name: ")
    player_name= input("player name: ")

    dice1 = randint(1,6)
    dice2 = randint(1,6)

    print(f"Dice 1:{dice1}")
    print(f"Dice 1:{dice2}")

get_dices()