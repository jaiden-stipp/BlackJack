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
if bet > balance:
    print("\nInvalid Bet, please try again")
    quit()
if bet == balance:
    print("Are you sure you'd like to proceed with betting your entire balance? Enter Y for yes and N for no\n")
    exit_or_play = input()
    if exit_or_play == "y" or exit_or_play == 'Y':
        pass
    else:
        print("\nThank you for playing")
        quit()
class Player():
    player_list = []

    def __init__(self, player_name, player_balance, player_bet = 0, player_hand = 0):
        self.name = player_name
        self.balance = player_balance
        self.hand = player_hand
        self.bet = player_bet
    def draw_card(self):
        card = random.randint(1,11)
        return card
    def end_game(self):
        print("\nThanks for playing!")
        quit()
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
        print("Total:")
        return self.hand
    
    def hit(self):
        card = Player.draw_card(self)
        self.hand += card
        print("\nCard Pulled:", card)
        print()
        if self.hand > 21:
            print("Total:", self.hand)
            print("\nBust!")
            quit()
        elif self.hand < 21:
            print(self.hand)
            return

        elif self.hand == 21:
            print("\nBlackJack!")
            quit()
            #win()
        else:
            print("You cannot hit")
    def stand(self):
        pass
    
player1 = Player(name, balance)
time.sleep(1)
print("Your Hand:")
print(player1.deal_hand())

print(player1.hit_stand())








   
        
    

class Dealer():
    def __init__(self, dealer_hand):
        self.hand = dealer_hand

