#input phase
LastName = input("Enter the last name ")
NumOfDependents = float(input("Enter the number of dependents "))
GrossIncome = float(input("Enter the gross income amount "))

#process phase
AdjustedGI = GrossIncome - NumOfDependents * 12000

if AdjustedGI > 50000:
    TaxRate = .2
else:
    TaxRate = .1

IncomeTax = AdjustedGI * TaxRate

if IncomeTax < 0:
    IncomeTax = 100

#output phase
print("The last name is ", LastName)
print("The gross income amount is ", GrossIncome)
print("The number of dependents is ", NumOfDependents)
print("The adjusted gross income amount ", AdjustedGI)
print("The income tax is ", IncomeTax)