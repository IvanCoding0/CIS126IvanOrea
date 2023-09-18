#input phase
PricePerShare = float(input("Enter price of share"))
CurrentPrice = float(input("Enter current price of stock"))
Quantity = float(input("Enter quantity being purchased"))

#process phase
Value = (CurrentPrice - PricePerShare) * Quantity

#output phase
print("Amount of your investment ", Value)