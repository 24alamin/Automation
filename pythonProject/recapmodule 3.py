salary = float(input("Enter your salary: "))
experiance = float(input("Enter your evperiance: "))
if experiance >= 5 and salary >=20000 :
    bonus = 0.05
    net_selary = salary + salary*bonus
    print("Your net selary with bonus", net_selary," USD")
else:
    print("You selary have only: ",salary, "USD")