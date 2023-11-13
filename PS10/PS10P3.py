def SalesReport(Sales):
    if Sales > 100000:
        Commission = Sales * .10
    else :
        Commission = Sales * .05
    NxtYrSales = Sales * .05
    return Commission, NxtYrSales

SalesPerson = input("Enter salesperson's last name: ")
Sales = float(input("Enter sales: "))
Commission, NxtYrSales = SalesReport(Sales)

print("Salesperson's last name ", SalesPerson)
print("This is the commision amount $ ", format(float(Commission), '10,.2f'))
print("This is next years target sales ", format(float(NxtYrSales), '10,.2f'))