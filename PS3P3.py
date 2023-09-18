#input phase
MealTotal = float(input("Enter the amount of the meal"))

#process phase
Tip15 = MealTotal * .15
Tip18 = MealTotal * .18
Tip20 = MealTotal * .2

Total15 = MealTotal + Tip15
Total18 = MealTotal + Tip18
Total20 = MealTotal + Tip20

#output phase
print("Amount for 15 %:")
print("Meal amount is: ", MealTotal)
print("Tip amount is: ", Tip15)
print("Total meal amount with tip: ", Total15)
print()

print("Amount for 18 %: ")
print("Meal amount is: ", MealTotal)
print("Tip amount is: ", Tip18)
print("Total meal amount with tip: ", Total18)
print()

print("Amount for 20 %: ")
print("Meal amount is: ", MealTotal)
print("Tip amount is: ", Tip20)
print("Total meal amount with tip: ", Total20)
print()