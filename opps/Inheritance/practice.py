class Animal:
    def sound(self):
        print("1 animal sound")
class Dog:
    def sound(self):
        print('Dog sound')
# a=Animal()
# a.sound()
# b=Dog()
# b.sound()

class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        print('B')
        super().show()
# a=A()
# a.show()
#
# b=B()
# b.show()
# print(B.mro())

class A:
    def display(self):
        print("A")
class B(A):
    def display(self):
        print("B")
        super().display()
class C(B):
    def display(self):
        print("C")
        super().display()
# a=C()
# a.display()
# print(C.mro())

class Vehicle:
    def wheels(self):
        print("V4")
class Car(Vehicle):
    def wheels(self):
        print("4")
class Bike(Vehicle):
    def wheels(self):
        print("2")

# a=Bike()
# a.wheels()
# b=Car()
# b.wheels()
# c=Vehicle()
# c.wheels()

class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def salary(self):
        print(f'{self.name} is getting salary of {self.base_salary}')
class Manager(Employee):
    def __init__(self,name,base_salary,hike):
        super().__init__(name,base_salary)
        self.hike=hike
    def salary(self):
        self.base_salary+=self.hike
        print(f'{self.name} is getting {self.base_salary}')

# e=Employee("Mani",25000)
# e.salary()
# m=Manager("Gayatri",50000,5000)
# m.salary()

class Uni:
    name='BVC'
    @classmethod
    def cv(cls):
        return "this is university"
class Clg(Uni):
    def cv2(self):
        return "this is clg"
# u=Uni()
# print(u.name)
# print(u.cv())
# c=Clg()
# print(c.cv2())
# print(c.name)


class Mathop:
    @staticmethod
    def add(a,b):
        return a+b
# class AdvMath(Mathop):
#     print("Adv")
# print(Mathop.add(5,2))
# print(AdvMath.add(10,13))

class Father:
    def skill(self):
        print("BIG")
class Mother:
    def skill(self):
        print("Beauty")
class Child(Father,Mother):
    pass

# c=Child()
# c.skill()
# print(Child.mro())


class Base_Acc:
    def withdraw(self,a):
        return a+5/100
class savings(Base_Acc):
    def withdraw(self,a):
        return super().withdraw(a+2/100)

class personal(savings):
    def withdraw(self,a):
        return super().withdraw(a+1/100)

# p=personal()
# print(p.withdraw(100))

class A:
    def m1(self):
        print('a')
class B(A):
    def m1(self):
        print('b')
        super().m1()
class C(B):
    def m1(self):
        print('c')
        super().m1()
# c=C()
# c.m1()
# print(C.mro())

class Employee:
    bonus=1000
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        return f'Employee details: {self.name} and salary {self.salary}.'
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        self.salary+=Manager.bonus
        return f'Manager details: {self.name} and salary {self.salary} and department of {self.department} '
# e=Employee('Mani',25000)
# print(e.display())
# m=Manager("Gayatri",50000,'EEE')
# print(m.display())

class person:
    def __init__(self,name):
        self.name=name
        print(f'{self.name} is a person')
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
        print(f'{self.name} is a student with {self.roll}')
p=person('mani')
s=student('gayatri',237)