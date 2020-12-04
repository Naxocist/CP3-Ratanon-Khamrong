def Vatcalculate(price):
    result = price + (price * 7/100)
    return result

price = int(input("Price to calculate vat: "))
print(Vatcalculate(price))