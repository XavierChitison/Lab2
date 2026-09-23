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
    while play_again.lower() == "y":

        print("\nTossing...")

        # Toss each player's coin
        player1.toss_coin()
        player2.toss_coin()

        # Get the results
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        # Display the results
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        # Determine the winner
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()

            print(f"...It's a Match! {player1.get_name()} wins a coin.")

        else:
            player2.win_coin()
            player1.lose_coin()

            print(f"...No Match! {player2.get_name()} wins a coin.")

        # Display current wallets
        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        # Optional Game Over feature
        if player1.get_wallet() == 0:
            print(f"\nGame Over! {player1.get_name()} ran out of coins.")
            break

        if player2.get_wallet() == 0:
            print(f"\nGame Over! {player2.get_name()} ran out of coins.")
            break

        # Ask if the user wants another round
        play_again = input("\nDo you want to toss the coins? (y/n): ")

    # Final results
    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")

    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")

    else:
        print("It's a draw!")


# Run the program
if __name__ == "__main__":
    main()