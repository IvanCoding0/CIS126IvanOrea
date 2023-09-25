#input phase
ApplianceName = input("Enter the appliance name ")
ApplianceCost = float(input("Enter the cost of the appliance "))
if ApplianceCost > 1000:
    Warranty = .1 * ApplianceCost
else:
    Warranty = .05 * ApplianceCost

#process phase
Total = ApplianceCost + Warranty

#output phase
print("The item name is ", ApplianceName)
print("The cost of the appliance ", ApplianceCost)
print("The warranty amount ", Warranty)
print("The total amount is ", Total)