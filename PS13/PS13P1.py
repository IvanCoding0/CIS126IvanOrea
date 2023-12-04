#define the object
class Employee:
    #use pass to leave empty for now
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        #self.rate = 0.0

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b
    #main - exceution starts here
    #instantiate the object
Employee1 = Employee('Ivan', 'Orea', 70000.00)

#use the object
#object syntax is object.method
print(Employee1.email)
print(Employee1.first)
print(Employee1.last)
print(Employee1.pay)
print(Employee1.bonus(0.1))
print(Employee1.bonus(0.2))