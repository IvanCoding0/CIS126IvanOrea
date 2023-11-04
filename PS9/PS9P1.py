NextMonthSales = 0


def CompForecast(Month, Sales):
    if Month == "Jan" or Month == "Feb" or Month == "Mar":
        ForecastPercent = .10
    elif Month == "Apr" or Month == "May" or Month == "Jun":
        ForecastPercent = .15
    elif Month == "Jul" or Month == "Aug" or Month == "Sep":
        ForecastPercent = .20
    elif Month == "Oct" or Month == "Nov" or Month == "Dec":
        ForecastPercent = .25
    Forecast = Sales * (1 + ForecastPercent)

    return Forecast


r = input("Do you want to calculate the sales forecast? (y/n) ")

while (r == "Y" or r == "y"):

    LastName = input("Enter last name ")
    Month = input("Enter the first three letters of the month ")
    Sales = float(input("Enter sales for the month "))

    NextMonthSales = CompForecast(Month, Sales)
    print(LastName, "sales forecast is $", NextMonthSales)
    print("       ")
    r = input("Do you want to calculate the sales forecast? (y/n) ")

print("       ")