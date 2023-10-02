#input phase
LastName = str(input("Enter the last name "))
Salary = float(input("Enter salary amount "))
JobLevel = float(input("Enter job level "))

#process phase

if JobLevel >= 10:
    BonusRate = .25
elif JobLevel >= 5:
    BonusRate = .2
else:
    BonusRate = .1

Bonus = Salary * BonusRate

#output phase
print("The employee last name is ", LastName)
print("The bonus amount is $", format(Bonus, ".2f"))