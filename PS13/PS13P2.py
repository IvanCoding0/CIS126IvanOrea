#define the object
class Student:
    #use pass to leave empty for now
    def __init__(self, first, last, DistrictCode, Credits):
        self.first = first
        self.last = last
        self.DistrictCode = DistrictCode
        self.Credits = Credits

    def Tuition(self):
        if self.DistrictCode == "I" or self.DistrictCode == "i":
            Tuition = self.Credits * 250.00
        else:
            Tuition = self.Credits * 500.00
        return Tuition
    #main - exceution starts here
    #instantiate the object
Student1 = Student('Ivan', 'Orea', 'I', 10)

#use the object
print(Student1.first)
print(Student1.last)
print(Student1.DistrictCode)
print(Student1.Credits)
print(Student1.Tuition())