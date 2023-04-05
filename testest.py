import random
hand = []
    
def draw_card():
    card = random.randint(1,12)
    print(card)
    hand.append(card)
    print(hand)
def calc_hand():
    temp = 0
    for i in hand:
        temp += i
    return temp
def check_win():
    if calc_hand() == 21:
        return "BlackJack!"
    if calc_hand() > 21:
        return False
    if calc_hand() < 21:
        return True
def hit():
    draw_card()
    if check_win():
        des = input("Enter 1 for Hit | Enter 2 for Stand\n")
        if des == 1:
            print("Hit Taken")
            hit()
        else:
            check_win()
            pass


hit()
print(calc_hand())