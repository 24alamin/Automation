user = [{
    "username":"1234",
    "password":"Alam",
    "role":"Admin"
},
    {"username":"Shakib",
     "password":"09876",
     "role":"Writer"},
    {"username":"Riyaz",
     "password":"389239",
     "role":"Reader"}]

for single in user:
    print(single.get("username"))