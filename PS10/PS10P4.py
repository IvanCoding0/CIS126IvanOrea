def BowlingAvg(Score1, Score2, Score3, Handicap):
    Total = Score1 + Score2 + Score3
    Average = (Total) / 3
    HandicapAvg = (Total + Handicap) / 3
    return  Average, HandicapAvg

LastName = input("What is bowlers last name? ")
Score1 = float(input("What was the first score? "))
Score2 = float(input("What was the second score? "))
Score3 = float(input("What was the third score? "))
Handicap = float(input("What is the bowlers handicap? "))
Average, HandicapAvg = BowlingAvg(Score1, Score2, Score3, Handicap)

print("Bowler last name: ", LastName)
print("Bowler average score is ", Average)
print("Bowler handicap average score is ", HandicapAvg)