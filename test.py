import random

class Player():
    def __init__(self):
        self.hand = []
    
    def draw_card(self):
        card = random.randint(1,12)
        print(card)
        self.hand.append(card)
        print(self.hand)
    def calc_hand(self):
        temp = 0
        for i in self.hand:
            temp += i
        return temp
    def check_win(self):
        if self.calc_hand() == 21:
                    print("BlackJack!")
    def hit(self):
        self.check_win()
        self.draw_card()
        if self.calc_hand() < 21:
            des = input("Enter 1 for Hit | Enter 2 for Stand\n")
            if des == 1:
                print("Hit Taken")
                self.hit()
            else:
                self.check_win()
                pass


player1 = Player()
player1.hit()
print(player1.calc_hand())
