person = [["Shakib","34","male","Bangladesh","shakib.com"],
["kohli","38","male","India","kohli.com"],
["Salma","25","female","Pakistan","salma.com"],
["Julia","29","female","England","julia.com"]]
i = 0
while i<len(person):
    single = person[i]
    name = single[0]
    age = single[1]
    gander = single[2]
    country = single[3]
    website = single[4]
    if gander == "male":
        pronoun = "He"
        relative = "His"
    else:
        pronoun = "She"
        relative = "Her"
    i = i+1
    bio = f"This is {name}. {pronoun} is {age} years old. {relative} birthplace is {country}. {relative} website name is {website}"
    print(bio)