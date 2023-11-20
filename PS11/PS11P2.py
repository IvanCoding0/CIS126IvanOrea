def DisplayArrays(LNames, Scores):
    for i in range (0, 10):
        print(LNames[i], Scores[i])

def RDisplayArrays(LNames, Scores):
    for i in range (9, -1, -1):
        print(LNames[i], Scores[i])

LNames = ["Wayne", "Potter", "Parker", "Jones", "Smith", "Bryant", "Johnson", "Adams", "Baker", "Davis"]
Scores = [100, 93, 95, 89, 85, 87, 82, 84, 83, 80]

print("original order ")
DisplayArrays(LNames, Scores)
print(" ")
print("reverse order")
RDisplayArrays(LNames, Scores)