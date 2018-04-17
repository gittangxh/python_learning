#coding=UTF-8

class SchoolMember:
    Quantity = 0
    def __init__(self, name, age, addrees):
        self.name = name
        self.age = age
        self.address = addrees
        SchoolMember.Quantity += 1

    def tell(self):
        print('Name:{} Age:{} Address:{}'.format(self.name,self.age, self.address), end=' ')

class Teacher(SchoolMember):
    def __init__(self, name, age, address, salary):
        SchoolMember.__init__(self, name, age, address)
        self.salary = salary
        print('Initialized Teacher:{}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, address, marks):
        SchoolMember.__init__(self, name, age, address)
        self.marks = marks
        print('Initialized Student:{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks:{}'.format(self.marks))


t=Teacher('tangxh', 31, 'jiulonghu', 100000)
s=Student('wanyw', 18, 'jiulonghu', 100)

t.tell()
s.tell()
print()
members = [t,s]
for member in members:
    member.tell()
