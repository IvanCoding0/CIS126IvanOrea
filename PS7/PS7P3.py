#Input Phase
file = open("PS7P3.txt", "r")
TotalBonus = 0
c = 0
LastName = file.readline()

#Process Phase
while LastName != "":
    Salary = file.readline()
    print()
    print("Employee Last Name: ", LastName)
    print("Employee salary: $", format(float(Salary), '10,.2f'))
    Bonus = float(Salary) * .1
    print("Employee Bonus: $:", format(Bonus, '10,.2f'))
    TotalBonus = TotalBonus + Bonus
    c = c + 1
    LastName = file.readline()
file.close()
AverageBonus = TotalBonus / c

#Output Phase
print("   ")
print("Average Bonus $", format(float(AverageBonus), '10,.2f'))
