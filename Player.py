"""
Program Name: Match Coins Game - Player Class
Author: Xavier Chitison
Purpose: This file contains the Player class. Each player has a name,
         a wallet of coins, and a Coin object that the player can toss.
Starter Code: No starter code was used.
Date: September 23, 2026
"""

from coin import Coin


class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()