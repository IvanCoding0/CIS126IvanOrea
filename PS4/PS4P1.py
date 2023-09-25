#input phase
ItemQuantity = float(input("Enter the item quantity"))
if ItemQuantity >= 1000:
    UnitPrice = 3.00
else:
    UnitPrice = 5.00

#process phase
ExtPrice = ItemQuantity * UnitPrice
Tax = .07 * ExtPrice
Total = ExtPrice + Tax

#output phase
print("The item quantity is ", ItemQuantity)
print("The unit price is ", UnitPrice)
print("The extended price is ", ExtPrice)
print("The tax amout is ", Tax)
print("The total Amount is ", Total)