"""
Program Name: Match Coins Game - Coin Class
Author: Xavier Chitison
Purpose: This file contains the Coin class. The Coin class represents
         a single coin that can be tossed and can land on Heads or Tails.
Starter Code: No starter code was used.
Date: September 23, 2026
"""
import random


class Coin:
    def __init__(self):
        # Start the coin on Heads
        self.__sideup = "Heads"
    def toss(self):
        # Generate either 0 or 1
        number = random.randint(0, 1)

        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup