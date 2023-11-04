TotalMarketValue = 0
TotalAssessedValue = 0

def CompAssessedValue(County, MarketValue):
    if County == "Cook" or County == "cook":
        AssesedValuePercent = .90
    elif County == "Dupage" or County == "dupage":
        AssesedValuePercent = .80
    elif County == "McHenry" or County == "mchenry":
        AssesedValuePercent = .75
    elif County == "Kane" or County == "kane":
        AssededValuePercent = .60
    else:
        AssesedValuePercent = .70

    AssesedValue = MarketValue * AssesedValuePercent

    return AssesedValue

r = input("Do you want to calculate assessed value (y/n) ")

while (r == "Y" or r == "y"):

    County = input("Enter the county ")
    MarketValue = float(input("Enter the home market value "))

    AssesedValue = CompAssessedValue(County, MarketValue)

    TotalMarketValue = TotalMarketValue + MarketValue
    TotalAssessedValue = TotalAssessedValue + AssesedValue

    print("Market value", MarketValue, "Assessed value", AssesedValue)

    r = input("Do you want to calculate assessed value (y/n) ")

print("Total Market Value", TotalMarketValue)
print("Total Assessed Value", TotalAssessedValue)