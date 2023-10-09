NumOfEmployees = 0
SumOfGrossPay = 0.0

Response=input("Do you want to start 'Yes or No' ")

while Response=="Yes" or Response=="yes":

    LastName = input("Enter employee last name: ")
    HoursWorked = float(input("Enter hours worked "))
    PayRate = float(input("Enter hourly pay rate "))
    GrossPay = HoursWorked * PayRate
    print(LastName, "gross pay amount is $", GrossPay)
    if HoursWorked >= 40:
        GrossPay = (PayRate * 40) + (HoursWorked - 40) * PayRate * 1.5
    SumOfGrossPay = SumOfGrossPay + GrossPay
    NumOfEmployees = NumOfEmployees + 1
    Response = input("Do you want to calculate average score 'Yes or No' ")

Average = SumOfGrossPay / NumOfEmployees
print("Sum of all gross pay ", SumOfGrossPay)
print("Number of Employess: ", NumOfEmployees)
print("Average gross pay ", Average)