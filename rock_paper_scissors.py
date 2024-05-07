
import random

list = ["rock", "paper", "scissors"]

player1score = 0
player2score = 0

rounds = int(input("How many rounds do you want to play?: "))

'''counter=0
while counter<rounds:
    counter+=1'''

for i in range(rounds):

    player1 = random.choice(list)
    player2 = input("Please choose your action: ")

    
    print("player1:",player1, "player2:",player2)

    if player1 == player2:
        print("Tie! Both players chose the same action.")

    elif player1 == "paper" and player2 == "rock":
         print("Player 1 wins!")
         player1score += 1
    elif player1 == "scissors" and player2 == "paper":
         print("Player 1 wins!")
         player1score += 1
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
        player1score += 1
    else:
        print("Player 2 wins!")
        player2score += 1

print("Player 1 score:", player1score)
print("Player 2 score:", player2score)

if player1score>player2score:
    print("Player 1 is winner of game.")
elif player1score==player2score:
    print("The game is tie")
else:
    print("Player 2 is winner of game.")