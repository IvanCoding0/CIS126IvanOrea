def DisplayArrays(LNames):
    for i in range (0, 10):
        print(LNames[i])

def RDisplayArrays(LNames):
    for i in range (9, -1, -1):
        print(LNames[i])

LNames = ["Wayne", "Potter", "Parker", "Jones", "Smith", "Bryant", "Johnson", "Adams", "Baker", "Davis"]

print("original order ")
DisplayArrays(LNames)
print(" ")
print("reverse order")
RDisplayArrays(LNames)