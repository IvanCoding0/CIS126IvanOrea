#Input Phase
PrincipleAmount = float(input("Enter principle amount "))
IntRate = float(input("Enter rate amount "))
TotalInt = 0

#Process Phase
print("Year       Beginning Balance       End Balance")

#Output Phase
for x in range (1, 6, 1):
    i = PrincipleAmount * IntRate
    TotalInt = TotalInt + i
    EndBalance = PrincipleAmount + i
    print (x, "          ", PrincipleAmount, "          ", EndBalance)
    PrincipleAmount = EndBalance

print("Total interest earned $", format(float(TotalInt), '10.2f'))