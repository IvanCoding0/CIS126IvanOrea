#Input Phase
file = open("PS7P3.txt", "r")
TotalBonus = 0
SumOfTotalBonus = 0
c = 0
LastName = file.readline()

#Process Phase
while LastName != "":
    Salary = file.readline()
    print()
    print("Employee Last Name: ", LastName)
    print("Employee salary: $", format(float(Salary), '10,.2f'))
    if float(Salary) >= 100000:
        Bonus = .2
    elif float(Salary) >= 50000:
        Bonus = .15
    else:
        Bonus = .1
    Bonus = float(Salary) * Bonus
    print("Employee Bonus: $", format(Bonus, '10,.2f'))
    TotalBonus = TotalBonus + Bonus
    c = c + 1
    LastName = file.readline()
file.close()
SumOfTotalBonus = SumOfTotalBonus + TotalBonus

#Output Phase
print("   ")
print("Sum of bonuses $", format(float(SumOfTotalBonus), '10,.2f'))