def PlayerData(LName, BattingAvg):
    f = open("Baseball.txt", "r")
    for i in range (0, 10,1 ):
        ln = f.readline()
        ln = ln.rstrip("\n")
        LName.append(ln)
        s = f.readline()
        s.rstrip("\n")
        BattingAvg.append(float(s))
    f.close()


def DArrays(LName, BattingAvg):
    for i in range(0, 10, 1):
        print(LName[i], " has a batting average of ", BattingAvg[i])


def SearchPlayer(PlayerName, LName, BattingAvg):
    found = False
    for i in range(0, 10, 1):
        if PlayerName == LName[i]:
            print("Player found")
            print("Last name ", LName[i])
            print("Batting average ", BattingAvg[i])
            found = True

    if not found:
        print("Player not found")

LastName = []
BattingAverage = []

PlayerData(LastName, BattingAverage)

DArrays(LastName, BattingAverage)

while True:
    SearchName = input("Enter a last name to search ")
    if SearchName == 'exit':
        break
    else:
        SearchPlayer(SearchName, LastName, BattingAverage)