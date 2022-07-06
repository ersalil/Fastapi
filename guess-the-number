import random

ans = random.randint(1,100)
lvl = 0

def guess_lvl():
    global lvl
    inp_lvl = input("What's your guess level? easy or hard: ")
    if inp_lvl == 'easy':
        lvl = 10
    else:
        lvl = 5
    guessing()

def guessing():
    global ans, lvl
    while(lvl>0):
        print("Guesses left", lvl)
        num = int(input("Guess the number: "))
        if num > ans:
            print("Guessed to high!")
        elif num < ans:
            print("Guessed to low!")
        else:
            print("Wollah!! You Guessed it right!")
            break
        lvl-=1

guess_lvl()