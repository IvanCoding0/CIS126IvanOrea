#input phase
FirstName = input("Enter first name ")
NumOfSteps = float(input("Enter number of steps taken in a day"))

#process phase
BurnedCalories = NumOfSteps * .25


#output phase
print("Walker's name ", FirstName)
print(" Your calories burned from walking ", BurnedCalories)