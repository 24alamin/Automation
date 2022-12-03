person = [["Moris","Male","Australia","1999","12342020"],
["John","Male","Canada","1987","12342323"],
["Kasim","Male","India","1922","12343345"],
["Nagin","Female","Ukraine","1939","12343330"],
["Saima","Female","Qatar","1998","12342222"],
["Rohima","Female","Soudi","1944","12343333"]]
i = 0
while i<len(person):
    single = person[i]
    name = single[0]
    gander = single[1]
    location = single[2]
    birthday = single[3]
    mobile = single[4]
    if gander == "Male":
        pronoun = "He"
        relative_pronoun = "his"
    else:
        pronoun = "She"
        relative_pronoun = "her"
    i= i+1
    bio = f"{name} is live in {location} {relative_pronoun} date of birth is {birthday} {relative_pronoun} number is {mobile}"
    print(bio)
