SumOfGrossPay = 0

def CompPayRate(JobCode, HoursWorked):
    GrossPay = JobCode * HoursWorked

r = input("Do you want to calculate the pay rate? (y/n) ")

while (r == "Y" or r == "y"):
    LastName = input("Enter employee last name: ")
    JobCode = input("Enter job code ")
    if JobCode == "L":
        PayRate = 25.00
    elif JobCode == "A":
        PayRate = 30.00
    elif JobCode == "J":
        PayRate = 50.00
    HoursWorked = float(input("Enter hours worked "))
    GrossPay = HoursWorked * PayRate

    if HoursWorked > 40:
        GrossPay = (PayRate * 40) + (HoursWorked - 40) * PayRate * 1.5
    SumOfGrossPay = SumOfGrossPay + GrossPay
    print(LastName, "gross pay amount is $", GrossPay)

    print("       ")
    r = input("Do you want to calculate the pay rate? (y/n) ")

print("The total gross pay is ", SumOfGrossPay)