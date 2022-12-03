import random
ludu = [1,2,3,4,5,6]
number = random.choice(ludu)
print(number)
if number == 6:
    print("you win the game!")
else:
    print(number,"Not win")