from random import randint
from time import sleep
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
suits = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
cards = { 1: 'Ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen', 13: 'King' }
class Player():
    def __init__(self, dealer):
        self.hand = []
        self.value = 0
        self.dealer = dealer
        
    def draw_card(self):
        suit_drawn = randint(0,3)
        card_drawn = randint(1,13)
        card = "{0} of {1}".format(cards[card_drawn], suits[suit_drawn])
        sleep(0.5)
        print("Your card is a {0}".format(card))
        self.hand.append(card)
        card_value = card_drawn
        if card_drawn == 11 or card_drawn == 12 or card_drawn == 13:
            card_value = 10
            self.value += card_value
        else: 
            self.value += card_value
        
    def check_hand(self):
        print("Your current hand: {0}".format(self.hand))
        sleep(1)
        print("Your current hand value: {0}".format(self.value))
        if self.value == 21:
            print("Congrats! You won!")
        if self.value > 21:
            print("Bust! Hand Value over 21")
        if self.value < 21:
            hitstand = input("Would you like to hit or stand (h/s): ")
            if hitstand == "h":
                self.hit()
            elif hitstand == "s":
                self.stand()
            else:
                print("Invalid Input, please try again")
                self.check_hand()
    def deal_in(self):
        self.draw_card()
        self.draw_card()
        self.check_hand()
    def hit(self): 
        self.draw_card()
        sleep(1)
        self.check_hand()
    def stand(self):
        self.dealer.dealer_draw()
        sleep(1)
        self.dealer.dealer_check()
        if self.dealer.dealer_value < 21:
            self.stand()

class Dealer():
    def __init__(self):
        self.dealer_hand = []
        self.dealer_value = 0
        self.player = Player(self)
    def dealer_draw(self):
        suit_drawn = randint(0,3)
        card_drawn = randint(1,13)
        card = "{0} of {1}".format(cards[card_drawn], suits[suit_drawn])
        print("\nDealer draws a {0}\n".format(card))
        self.dealer_hand.append(card)
        card_value = card_drawn
        if card_drawn == 11 or card_drawn == 12 or card_drawn == 13:
            card_value = 10
            self.dealer_value += card_value
        else: 
            self.dealer_value += card_value
    def dealer_check(self): 
        print("Dealer's current hand: {0}".format(self.dealer_hand))
        print("Dealer's current hand value: {0}".format(self.dealer_value))
        if self.dealer_value > 21:
            print("Dealer went over 21!\n")
            print("\nYou won!")
        elif self.dealer_value > self.player.value:
            print("Dealer wins!")
            
        elif self.dealer_value == 21:
            print("Dealer wins!")
        
        
    def start_game(self):
        self.dealer_draw()
        self.player.deal_in()


    
    



dealer = Dealer()
print(logo + "\n\n")
print("Welcome!")
str(input("Enter any character to continue \n"))
dealer.start_game()
print("\n")



