
usd = input("Enter USD amount: ")
usd_number = float(usd)
exchange_rate = 100
bdt = usd_number * exchange_rate
paragraph = str(usd_number) + " USD is equal to " + str(bdt) + "BDT"
print(paragraph)
