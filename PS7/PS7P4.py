#Input Phase
file = open("PS7P4.txt", "r")

c = 0
TotalEp = 0

Item = str(file.readline().rstrip('\n'))

#Process Phase

while Item != "":
  Quantity = float(file.readline())
  Price = float(file.readline())

  ExtPrice = Quantity * Price

  TotalEp = TotalEp + ExtPrice
  c = c + 1

  print("Item ", Item)
  print("Quantity amount ", Quantity)
  print("Price ", Price)
  print("Extended price is $", ExtPrice)
  print("       ")

  Item = str(file.readline().rstrip('\n'))
Average = TotalEp / c

#Output Phase
print("Total extended prices $", TotalEp)
print("Total count of items ", c)
print("Average order", Average)