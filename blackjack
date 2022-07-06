import random
from turtle import clear
global cards, dealer, player

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer = []
player=[]

def new_card():
    return int(random.choice(cards))

def initializer():
    dealer.append(new_card())
    player.append(new_card())
    player.append(new_card())
    game()

def hit():
    player.append(new_card())
    if(sum(player)>21) or (sum(dealer)>21):
        if sum(player)>21:
            try:
                player[player.index(11)]=1
            except:
                pass
        final()
    
    game()

def stand():
    while(sum(dealer)<17):
        dealer.append(new_card())
    final()

def game():
    print_status()
    res = input("Type 'h' to hit or 's' to stand:")
    if res == 'h':
        hit()
    else:
        stand()


def final():
    print_status()
    if sum(dealer)>21 or sum(player)>21:
        if sum(dealer)>21:
            print("Player Wins!!")
        else:
            print("Dealer Wins!!")
    elif (sum(dealer) > sum(player)):
        print("Dealer Wins!!")
    elif (sum(dealer) < sum(player)):
        print("Player Wins!!")
    else:
        print("Draw")
    play_again()

def play_again():
    if input("\n\nTo play again type 'y' else 'n':  ") == 'y':
        dealer.clear()
        player.clear()
        initializer()
        print("\n\n")

def print_status():
    print("Dealer's Game: ",dealer, " \n", "Total: ", sum(dealer))
    print("Your Game: ",player, " \n", "Total: ", sum(player))

initializer()
