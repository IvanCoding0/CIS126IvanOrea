TotalGallons = 0

def CompSquareFootage(Length, Width, Height):
    SquareFootage = 2 * Length * Width + 2 * Length * Height + 2 * Width * Height

    return SquareFootage

r = input("Do you want to calculate the square footage? (y/n) ")

while (r == "Y" or r == "y"):

    Length = float(input("Enter the length of the room "))
    Width = float(input("Enter the width of the room "))
    Height = float(input("Enter the height of the room "))

    SquareFootage = CompSquareFootage(Length, Width, Height)
    Gallons = SquareFootage / 50

    print("The square footage of the room is ", SquareFootage)
    print("The gallons of paint needed are ", Gallons)
    TotalGallons = TotalGallons + Gallons
    print("       ")

    r = input("Do you want to calculate the square footage? (y/n) ")

print("The total gallons of paint needed ", TotalGallons)