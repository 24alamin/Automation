number = int(input("Enter your number: "))
if number >= 80 and number <= 100:
    print("You got A+")
elif number >=70 and number <= 79:
    print("You got A")
elif number <=69 and number >=0:
    print("Sorry you are fail!")
else:
    print("This is invalid number")