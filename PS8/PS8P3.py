Counter = 0

def CompMPG(MilesTrav, GallonsUsed):
    MPG = MilesTrav / GallonsUsed
    return MPG


r = input("Do you want to calculate the MPG? (y/n) ")

while (r == "Y" or r == "y"):
    City = input("Enter the city destination ")
    MilesTrav = float(input("Enter miles traveled "))
    GallonsUsed = float(input("Enter gallons used "))
    MPG = CompMPG(MilesTrav, GallonsUsed)
    Counter = Counter + 1
    print(City, "MPG:", MPG)

    print("       ")
    r = input("Do you want to calculate the MPG? (y/n) ")

print("       ")

print("Counter is ", Counter)