def CompExtPrice(Quantity, UnitPrice):
    ExtPrice = Quantity * UnitPrice

    if ExtPrice > 100000:
        DiscountAmt = ExtPrice * .1
    else:
        DiscountAmt = 0

    return ExtPrice


TotalExtPrice = 0
r = input("Do you want to computer the extended price? (y/n) ")

while (r == "Y" or r == "y"):
    Quantity = float(input("Enter quantity: "))
    UnitPrice = float(input("Enter unit price: "))
    ExtPrice = CompExtPrice(Quantity, UnitPrice)
    TotalExtPrice = TotalExtPrice + ExtPrice
    print("Extended price is $", ExtPrice)
    r = input("Do you want to computer the extended price? (y/n) ")

print("Total extended price is $", TotalExtPrice)