"""
Program Name: Match Coins Game
Author: Xavier Chitison
Purpose: This program creates two players and allows them to play
         a coin matching game. If both coins match, Player 1 wins
         a coin. If the coins do not match, Player 2 wins a coin.
         The game continues until the user quits or a player runs
         out of coins.
Starter Code: No starter code was used.
Date: September 23, 2026
"""

from player import Player


def main():
    # Create the two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    # Ask the user if they want to start
    play_again = input("\nDo you want to toss the coins? (y/n): ")
