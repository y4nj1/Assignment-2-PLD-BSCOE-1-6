appleprice = 20
orangeprice = 25

print("The price of an apple is 20 pesos.")
print("The price of an orange is 25 pesos.")

quantiapple = int(input("How many apples would you like to buy? "))
quantiorange = int(input("How many oranges would you like to buy? "))

amountapple = appleprice * quantiapple
amountorange = orangeprice * quantiorange
amounttotal = amountapple + amountorange

print(f"The total amount is {amounttotal} pesos.")