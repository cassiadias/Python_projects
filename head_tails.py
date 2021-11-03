import random

print("--WELCOME TO COIN TOSS GAME--")

coin_toss = input('To get started, click "Enter" on your keyboard\n')

random_coin = random.randint(0,1)

if random_coin == 1:
    print("Heads")

else:
    print("Tails")
