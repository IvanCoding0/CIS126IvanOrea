Total = 0
Tax = 0

def CompTotal (Quantity, Price):
    global Total
    Total = Quantity * Price
    global Tax
    Tax = Total * .07
    return

Quantity = float(input("Enter quantity amount "))
Price = float(input("Enter price "))
CompTotal (Quantity, Price)

print("The total is ", format(float(Total), '10,.2f'))
print("The tax is ", format(float(Tax), '10,.2f'))