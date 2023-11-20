def loadarrays (LName, Salary):
    f = open("salary.txt", "r")
    for i in range (0, 10,1 ):
        ln = f.readline()
        ln = ln.rstrip("\n")
        LName.append(ln)
        s = f.readline()
        s.rstrip("\n")
        Salary.append(float(s))
    f.close()
def DArrays (LName, Salary):
    for i in range (0, 10,1 ):
        print(LName[i], " has a salary of ",Salary[i])

def HiLow(LName, Salary):
    HighSalary = 0.0
    HighSub = 0
    LowSalary = 999
    LowSub = 0

    for i in range (0, 10,1 ):
        if (Salary[i] > HighSalary):
            HighSalary = Salary[i]
            HighSub = i
        elif Salary[i] < LowSalary:
            LowSalary = Salary[i]
            LowSub = i

    print(LName[HighSub], " has the highest salary at ", Salary[HighSub])
    print(LName[LowSub], " has the lowest salary at ", Salary[LowSub])

def DisplayArrays(LName, Salary):
    for i in range (0, 10,1 ):
        print(LName[i], " has a salary of ",Salary[i])

    print("Another display using for loops")
    for x in range(2, 10, 1):
        print(LName[x])

        for j in LName:
            print(j)

def Rdisplay(Lname):
    for i in range (4, -1, -1):
        print(Lname[i])

Lname = []
Salary = []
loadarrays(LName, Salary)
DArrays(LName, Salary)
HiLow(LName, Salary)
DisplayArrays(LName, Salary)
Rdisplay(LName)