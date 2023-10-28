TotalTuition = 0


def CompTuitionOwed(CreditHours, DistrictCode):

    TuitionOwed = CostPerCredit * CreditHours

    return TuitionOwed


r = input("Do you want to calculate the tuition amount owed? (y/n) ")

while (r == "Y" or r == "y"):
    LastName = input("Enter student last name ")
    DistrictCode = input("Enter district code ")
    CreditHours = float(input("Enter credit hours "))
    CostPerCredit = 250.00 if DistrictCode == "I" or DistrictCode == "i" else 550.00
    TuitionOwed = CompTuitionOwed(CreditHours, DistrictCode)
    TotalTuition = TotalTuition + TuitionOwed
    print(LastName, "tuition amount is $", TuitionOwed)
    print("       ")
    r = input("Do you want to calculate the tuition amount owed? (y/n) ")

print("       ")

print("Sum of total tuition amount is $ ", TotalTuition)