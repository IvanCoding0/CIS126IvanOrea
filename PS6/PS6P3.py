Counter = 0
TotalEx1 = 0.0

Response = input("Do you want to calculate average score 'Yes or No' " )
while(Response=="Yes" or Response=="yes"):
	Counter = Counter + 1
	LastName = input("Enter student last name ")
	Score1=float(input("Enter exam score 1 "))
	Score2=float(input("Enter exam score 2 "))
	Average=(Score1 + Score2) / 2
	print(LastName, " has average of ", Average)
	TotalEx1 = TotalEx1 + Score1
	Response = input("Do you want to calculate average score 'Yes or No'")

AverageEx1 = TotalEx1 / Counter
print("Number of students: ", Counter)
print("Average exam score 1 ", AverageEx1)