marks = int(input("Enter your mark: "))
weight = int(input("Enter your weight: "))
if not (marks <= 80 or weight >= 20):
    print("you got a choclate!")
else:
    print("You have less marked or over weight")