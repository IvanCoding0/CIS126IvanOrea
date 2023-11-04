TotalMSRP = 0
TotalSalePrice = 0

def CompOutTheDoorPrice(MSRP, Make, Model, EVCode):
    if Make == "Honda" or Make == "honda" and Model == "Accord" or Model == "accord":
        PercentOff = 0.10
    elif Make == "Toyota" or Make == "toyota" and Model == "Rav4" or Model == "rav4":
        PercentOff = 0.15
    elif EVCode == "Y" or EVCode == "y":
        PercentOff = 0.30
    else:
        PercentOff = 0.05

    Discount = MSRP * PercentOff
    NewMSRP = MSRP - Discount
    OutTheDoorPrice = NewMSRP + 0.07 * NewMSRP

    return OutTheDoorPrice

r = input("Do you want to calculate the out of the door price (y/n) ")

while (r == "Y" or r == "y"):

        Make = input("Enter make of the automobile: ")
        Model = input("Enter model of the automobile: ")
        EVCode = input("Is it an electric vehicle? (Y or N): ")
        MSRP = float(input("Enter the MSRP of the vehicle: "))

        OutTheDoorPrice = CompOutTheDoorPrice(MSRP, Make, Model, EVCode)
        TotalMSRP = TotalMSRP + MSRP
        TotalSalePrice = TotalSalePrice + OutTheDoorPrice

        print("Out the door price for ", Make, Model,"is $", OutTheDoorPrice)

        r = input("Do you want to calculate the out of the door price (y/n) ")

print("Total MSRP of all cars: ", TotalMSRP)
print("Total sales price of all cars", TotalSalePrice)