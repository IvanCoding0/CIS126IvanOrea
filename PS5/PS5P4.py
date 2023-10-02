#input phase
ConcertTickets = float(input("Enter number of tickets "))

#proccess phase
if ConcertTickets >= 25:
  PricePerTik = 50
elif ConcertTickets >= 10:
  PricePerTik = 60
elif ConcertTickets >= 5:
  PricePerTik = 70
else:
  PricePerTik = 75
Total = ConcertTickets * PricePerTik

#output phase
print("Number of tickets: ", ConcertTickets)
print("Price per ticket: ", PricePerTik)
print("Total: ", Total)