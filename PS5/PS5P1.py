#input phase
QuantityWidget = float(input("Enter the quantity of widgets "))

#proccess phase
Price = 10 \
    if QuantityWidget > 10000 \
    else 20 \
    if QuantityWidget > 5000 \
    else 30
ExtendedPrice = QuantityWidget * Price
Tax = ExtendedPrice * .07
Total = ExtendedPrice + Tax

#output phase
print("Extended Price: $", ExtendedPrice)
print("Tax Amount: $", format(Tax, ".2f"))
print("Total: ", Total)