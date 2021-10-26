moneyavail = int(input("How much money do you have? "))

appleprice = int(input("How much is an apple? "))
applequanti = moneyavail // appleprice
change = moneyavail % appleprice
print(f"You can buy {applequanti} apples and your change is {change} pesos.")
