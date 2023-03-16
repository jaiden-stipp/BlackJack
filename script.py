import time
import random
#Intro text
logo = """
\n-----------------------------------------------------------------------------------------
$$$$$$$\  $$\        $$$$$$\   $$$$$$\  $$\   $$\   $$$$$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$ | $$  |  \__$$ |$$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|$$ |$$  /      $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$\ |$$ |      $$$$$$$$ |$$ |      $$$$$  /       $$ |$$$$$$$$ |$$ |      $$$$$  /  
$$  __$$\ $$ |      $$  __$$ |$$ |      $$  $$<  $$\   $$ |$$  __$$ |$$ |      $$  $$<   
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\ $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$$$$$$  |$$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ | \$$\\$$$$$$  |$$ |  $$ |\$$$$$$  |$$ | \$$\ 
\_______/ \________|\__|  \__| \______/ \__|  \__|\______/ \__|  \__| \______/ \__|  \__|
 ----------------------------------------------------------------------------------------                                                                                        
                                                                                         """
print(logo + "\n\n")
print("Hello! Please enter your name below: \n")
name = str(input())
print("\nWelcome " + name + "!\n")
time.sleep(1)
print("How much money are you putting on the table today?\n")
balance = float(input())
print("\nCurrent Balance: ${}\n".format(balance))
time.sleep(1)
bet = 0
print("How much would you like to bet on the current game?\n")
bet_input = input()
bet += float(bet_input)
if bet > game_balance:
    print("\nInvalid Bet, please try again")
    quit()
if bet == game_balance:
    print("Are you sure you'd like to proceed with betting your entire balance? Enter Y for yes and N for no\n")
    exit_or_play = input()
    if exit_or_play == "y" or exit_or_play == 'Y':
        pass
    else:
        print("\nThank you for playing")
        quit()
class Player():
    player_list = []

    def __init__(self, player_name, player_balance, player_bet, player_hand = 0):
        self.name = player_name
        self.balance = player_balance
        self.hand = player_hand
        self.bet = player_bet
    def draw_card(self):
        card = random.randint(1,11)
        return card
    def deal_hand(self):
        card1 = Player.draw_card(self)
        card2 = Player.draw_card(self)
        self.hand += card1
        self.hand += card2
        print(card1, card2)
        if self.hand > 21:
            return "Bust!"
        if self.hand == 21:
            self.balance += self.bet
            return "Blackjack!"
        return self.hand
player1 = Player(name, balance, final_bet)
print(player1.deal_hand())



def hit():
    if player_hand < 21:
        card = draw_card()
        player_hand += card
        if player_hand > 21:
            print("\nBust!")
        elif player_hand == 21:
            print("\nBlackJack!")
            #win()
    else:
        print("You cannot hit")


class Player():
    player_name = name
    player_balance = balance
    def __init__(self, hand, money, bet):
        pass
   
        
    

class Dealer():
    pass


