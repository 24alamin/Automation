import random
person = ["Rohim","30","Dhaka","Sima"]
name = person[0]
age = person[1]
address = person[2]
wife = person[3]

group_one = [
    f"This is {name}.",
    f"My name is {name}.",
    f"{name} is my name.",
    f"I am {name}."
]

group_two = [
    f"I live in {address}",
    f"{address} is my town.",
    f"{address} is where I born.",
    f"I rised in {address}."
]

group_one = random.choice(group_one)
group_two = random.choice(group_two)

bio = f"{group_one} {group_two}"
print(bio)