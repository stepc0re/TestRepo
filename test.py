import sys


class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

    # instead of Name ein __str__ , i say print x nicht x. Name, str wird automatisch benutzt
    def __str__(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

#
# class Fahrzeug:
#     def __init__(self, rader, geschwindigkeit):
#         self.numrader = rader
#         self.speed = geschwindigkeit
#
#     def Geschwindigkeit(self):
#         return self.speed
#
# class Motor(Fahrzeug):
#     def __init__(self, rader, geschwindigkeit, motor):
#         Fahrzeug.__init__(self, rader, geschwindigkeit)
#         self.kindofmotor = motor
#
#
#     def getmotor(self):
#         return self.numrader + self.speed
#
# x = Fahrzeug(4, 200)
# y = Motor(2, 200, "diesel")
#
# print(x.numrader())
# print(y.getmotor())

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum
# overridden die str von Person class
    def __str__(self):
        return super().__str__() + ", " +  self.staffnumber


x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x)
print(y)