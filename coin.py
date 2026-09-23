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
