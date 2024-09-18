# START
import random

player1: str = input("Enter the name of player 1: ")
player2: str = input("Enter the name of player 2: ")
player3: str = input("Enter the name of player 3: ")
player4: str = input("Enter the name of player 4: ")
winner = random.choice((player3, player4, player2, player1))
print(f"the winner is {winner}")
