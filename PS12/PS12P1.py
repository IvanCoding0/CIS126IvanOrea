# Step 1 prompting user for number of items in list
NumbersForList = int(input("Enter the number of items for the list "))

NumberList = []
for i in range(NumbersForList):
    NumberList.append(int(input("Enter integer ")))
print("List:", NumberList)

# Step 2 - inserting 99 at position 1
NumberList.insert(0, 99)
print("Updated list after entering 99 at position 1: ", NumberList)

# Step 3 - replacing 99 with 100
NumberList[NumberList.index(99)] = 100
print("Updated list after replacing 99 with 100: ", NumberList)

# Step 4 - creating a second list of numbers
NumberList2 = [500, 600, 700, 800, 900]
print("Second set of numbers for list: ", NumberList2)
NumberList.extend(NumberList2)
print("List after extending with the second list: ", NumberList)

# Step 5 - removing 800
NumberList.remove(800)
print("List after removing 800: ", NumberList)

# Step 6 - removing the third item
del NumberList[2]
print("List after removing the third item: ", NumberList)

# Step 7 - create a list of grades
GradesList = ["A", "B", "C", "A", "A", "C"]

# Step 8 - display a count of the number of A grades
GradesCount = GradesList.count("A")
print("Number of grades containing A: ", GradesCount)

# Step 9 - display the index of the first B grade
IndexForGrade = GradesList.index("B")
print("Index of the first B grade: ", IndexForGrade)

# Step 10 - look for grade F in grades list then display message if not in list
if "F" not in GradesList:
    print("Grade F is not in the grades list ")

# Step 11 - clear the second list
NumberList2.clear()
print("Second list after being cleared: ", NumberList2)

# Step 12 - delete the second list
del NumberList2
try:
    print(NumberList2)
except NameError:
    print("NumberList2 is not defined anymore after being deleted")

# Step 13 - Create a list of players
Players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# Step 14 - sort list of players
Players.sort()
print("List of sorted players: ", Players)

# Step 15 - make a copy of the list of players
Players2 = Players.copy()
print("Copy of the list of the players list is named Players2: ", Players2)

# Step 16 - reverse the list
Players2.reverse()
print("Original players: ", Players)
print("Reversed order of the list of Players2: ", Players2)