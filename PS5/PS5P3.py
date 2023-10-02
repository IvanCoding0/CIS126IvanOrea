#input phase
PrincipleAmount = float(input("Enter principle amount "))
Maturity = float(input("Enter years to mature "))

#proccess phase
if PrincipleAmount > 100000 and Maturity == 5:
  InterestRate = .06
elif PrincipleAmount >=50000 and Maturity == 10:
  InterestRate = .05
elif PrincipleAmount >= 50000 and Maturity == 5:
  InterestRate = .04
else:
  InterestRate = .02
FirstYearInterest = PrincipleAmount * InterestRate

#output phase
print("Principle: ", PrincipleAmount)
print("Intrest Rate: ", InterestRate)
print("First Year Intrest: ", FirstYearInterest)