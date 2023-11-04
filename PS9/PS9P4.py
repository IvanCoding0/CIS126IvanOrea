TotalPrice = 0

def CompTicketPrice(Miles):
    if Miles >= 30:
        Price = 12
    elif Miles >= 20:
        Price = 10
    elif Miles >= 10:
        Price = 8
    else:
        Price = 5
    return Price

r = input("Do you want to calculate train ticker price (y/n) ")

while (r == "Y" or r == "y"):

    LastName = input("Enter last name: ")
    Miles = float(input("Enter miles from downtown Chicago: "))
    TickerPrice = CompTicketPrice(Miles)
    TotalPrice = TotalPrice + TickerPrice
    print("Ticket price for", LastName, "$", TickerPrice)

    r = input("Do you want to calculate train ticker price (y/n) ")

print("Total price for all tickets $", TotalPrice)