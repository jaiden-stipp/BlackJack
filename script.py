import random
#Intro text
player_hand = 0
dealer_hand = 0
def play():
    pass
print("Hello! Please enter your name below: \n")
name = str(input())
print("\nWelcome " + name + "!\n")
print("How much money are you putting on the table today?\n")
balance = float(input())
print("\nCurrent Balance: ${}".format(balance))

def hit():
    card = randint(1,12)
    player_hand += card
    if player_hand > 21:
        print("\nBust!")
    elif player_hand == 21:


class Player():
    player_name = name
    player_balance = balance
    def __init__(self, hand, money, bet):
        pass
   
        
    

class Dealer():
    pass


