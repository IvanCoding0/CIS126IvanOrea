#input phase
NumberOfBooks = int(input("Enter the number of books "))
CostPerBook = float(input("Enter the cost per book "))

#process phase
OrderTotal = NumberOfBooks * CostPerBook

if OrderTotal > 50:
    Shipping = 0
else:
    Shipping = 25

#output phase
print("The order total is ", OrderTotal)
print("The shipping cost is ", Shipping)