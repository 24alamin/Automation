# natural_body_tempareture = 98.4
# temparature = float(input("Enter your body temperature: "))
# if temparature >= natural_body_tempareture:
#     print(" You have fiver and you should go to doctor.")
# else: print("You're completely fine.")
name = input("Enter your name: ")
gander = input("Enter gander (m/f): ")
country = input("Enter your country: ")
if gander == "m":
    profession = "Actor"
    problem = "He"
    pronoun = "Kicchu pare na"
    known = "Naiok"
else:
    profession = "Actress"
    problem = "She"
    pronoun = "Shob pare"
    known = "Naika"

print(f"{name} is a {profession}. {problem} live in {country}. {problem} known as {known} and the problem is {pronoun}")