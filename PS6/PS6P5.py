SumOfDiscountAmount = 0

Response = input("Do you want to calculate total order with discounts? 'Yes or No ' " )

while Response=="Yes" or Response=="yes":
    Quantity = float(input("Enter quantity amount "))
    Price = float(input("Enter price amount "))
    ExtPrice = Quantity * Price
    DiscountedAmount = ExtPrice * 0.25 \
        if ExtPrice > 10000.00 \
        else ExtPrice * 0.10
    Total = ExtPrice - DiscountedAmount
    SumOfDiscountAmount = SumOfDiscountAmount + DiscountedAmount


    print("Extended Price amount is $", ExtPrice)
    print("Discounted amount is $", DiscountedAmount)
    print("Total order amount is $", Total)
    Response = input("Do you want to calculate average score 'Yes or No'")


print("The sum of all discounts is $", SumOfDiscountAmount)