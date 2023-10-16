#Input Phase
with open("PS7P5.txt", "r") as file:
    c = 0
    TotalTuition = 0
    LastName = file.readline()
    #Process Phase
    while LastName != "":
        DistrictCode = str(file.readline().rstrip('\n'))
        Credits = float(file.readline())
        CostPerCredit = 250.0 if DistrictCode == "I" or DistrictCode == "i" else 500.0
        Tuition = CostPerCredit * Credits
        c = c + 1
        TotalTuition = TotalTuition + Tuition
        print("Student ", LastName)
        print("Credits taken ", Credits)
        print("Tuition owed ", Tuition)
        print("       ")

        LastName = str(file.readline().rstrip('\n'))
    #Output Phase
    print("Number of students ", c)
    print("Total tuition owed $", format(float(TotalTuition), '10,.2f'))