import random
number = [1,2,3,4,5,6,7,8,9,0]
print("Let's play choose number between 0-9:")
print("*"*10,"-"*14,"*"*10)
computer = random.choice(number)
while True:
    number = int(input("Enter your number: "))
    if number == computer:
        print("congratulations!")
        break
    else:
        print("Hoy nai!")