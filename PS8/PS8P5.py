TotalTuition = 0


def CompTuitionOwed(CreditHours, DistrictCode):
    TuitionOwed = CreditHours * DistrictCode

    CostPerCredit = 250.0 if DistrictCode == "I" or DistrictCode == "i" else 550.0
    Tuition = CostPerCredit * CreditHours

    return TuitionOwed


r = input("Do you want to calculate the tuition amount owed? (y/n) ")

while (r == "Y" or r == "y"):
    LastName = input("Enter student last name ")
    TuitionOwed = CompTuitionOwed(CreditHours, DistrictCode)
    TotalTuition = TotalTuition + TuitionOwed
    print(LastName, "tuition amount is $", TuitionOwed)
    print("       ")
    r = input("Do you want to calculate the batting average? (y/n) ")

print("       ")

print("Sum of total tuition amount is $ ", TotalTuition)