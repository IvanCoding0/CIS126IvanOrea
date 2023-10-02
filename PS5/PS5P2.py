#input phase
PartNumber = int(input("Enter the part Number "))
Quantity = float(input("Enter Quantity amount "))

#proccess phase
if PartNumber == 10 or PartNumber == 55:
  UnitCost = 1.00
elif PartNumber == 99:
  UnitCost = 2.00
elif PartNumber == 80 or PartNumber == 70:
  UnitCost = 3.00
else:
  UnitCost = 5.00
Total = Quantity * UnitCost

#output phase
print("Part number: ", PartNumber)
print("Unit Price: ", UnitCost)
print("Total: ", Total)