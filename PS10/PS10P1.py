def Discount(Quantity, Price, DiscountRate):
    Total = (Quantity * Price)
    DiscountAmount = DiscountRate * Total
    DiscountPrice = Total - DiscountAmount

    return DiscountAmount, DiscountPrice

Quantity = float(input("Enter Quantity: "))
Price = float(input("Enter the unite Price $ "))
DiscountRate = float(input("Enter the Discount Rate % "))
DiscountAmount, DiscountPrice = Discount(Quantity, Price, DiscountRate)

print("This is your quantity: ", Quantity)
print("this is your price $", format(float(Price), '10.2f'))
print("this is your discount rate $", format(float(DiscountRate), '10.2f'))
print("this is your discount amount $", format(float(DiscountAmount), '10.2f'))
print("this is your discount price $", format(float(DiscountPrice), '10.2f'))
