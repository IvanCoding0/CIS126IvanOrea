#input phase
FixedCost = float(input("Enter the fixed cost amount"))
PricePerUnit = float(input("Enter the price per unit"))
CostPerUnit = float(input("Enter the cost per unit"))

#process phase
BreakEven = FixedCost / (PricePerUnit - CostPerUnit)


#output phase
print("The amount to break even ", BreakEven)