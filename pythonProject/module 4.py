user = ["John Doe", 56, True, "Kamrup Kamakkha"]
# print(user[-4], user[-4], sep="----")
# print(user[-3], user[-3], sep="-----")
# print(user[-2],user[-2], sep="-----")
# print(user[-1],user[-1],sep="-----")
name = user[0]
age = user[1]
location = user[3]
if_male = user[2]
if if_male:
    pronoun = "He"
    gander = "Male"
else:
    pronoun = "She"
    gander = "Female"
    sentence = f"{name} {pronoun} is a {age} years old {gander} who live in {location}"
    print(sentence)