Counter = 0
def CompBattingAvg(NumOfHits, AtBats):
  BattingAvg = NumOfHits / AtBats
  return BattingAvg

r = input("Do you want to calculate the batting average? (y/n) ")

while (r == "Y" or r == "y"):
  LastName = input("Enter last name ")
  NumOfHits = float(input("Enter number of hits "))
  AtBats = float(input("Enter at bat attempts "))
  BattingAvg = CompBattingAvg(NumOfHits, AtBats)
  Counter = Counter + 1
  print("Batting Average for ", LastName, " is ", BattingAvg)
  print("       ")
  r = input("Do you want to calculate the batting average? (y/n) ")

print("       ")

print("Counter is ", Counter)