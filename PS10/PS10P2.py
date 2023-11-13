def ExamAvg(Exam1, Exam2, Exam3):
    Average = (Exam1 + Exam2 + Exam3) / 3
    TotalPoints = Exam1 + Exam2 + Exam3

    return TotalPoints, Average

LastName = input("Enter the student last name ")
Exam1 = float(input("Enter Exam 1 Score "))
Exam2 = float(input("Enter Exam 2 Score "))
Exam3 = float(input("Enter Exam 3 Score "))

TotalPoints, Average = ExamAvg(Exam1, Exam2, Exam3)

print("Student last name: ", LastName)
print("Total points: ", TotalPoints)
print("Average Score is: ", Average)