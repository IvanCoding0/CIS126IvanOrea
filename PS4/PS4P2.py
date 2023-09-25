#input phase
Item = input("Enter the item A or B: ")
Quantity = float(input("Enter the quantity"))
if Item == "A":
    UnitPrice = 10.00
else:
    UnitPrice = 20.00

#process phase
ExtPrice = Quantity * UnitPrice

#output phase
print("The item is ", Item)
print("The unit price is ", UnitPrice)
print("The extended price is ", ExtPrice)