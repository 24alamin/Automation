import random
number = [0,1,2,3,4,5,6,7,8,9]
print("Let's play the game!")
print("-"*6,"*"*5,"-"*6)
computer = random.choice(number)
while True:
    number = int(input("Enter your number:"))
    if computer == number:
        print("Congratulation!")
        break
    else:
        print("Hoy nai!")