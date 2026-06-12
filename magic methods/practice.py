class Student:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def __str__(self):
        return f'student name is {self.name}, age is{self.age}'
a=Student('mani',22)
# print(a)

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        return self.x + o2.x
# a=A(10)
# b=A(20)
# print(a+b)


class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,o2):
        return A(self.x + o2.x)
    def __str__(self):
        return str(self.x)

# a=A(10)
# b=A(20)
# c=A(30)
# print(a+b+c)

class V:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o2):
        return self.x + o2.x, self.y + o2.y
    def __eq__(self,o2):
        return self.x == o2.x, self.y == o2.y
    def __sub__(self,o2):
        return self.x - o2.x, self.y - o2.y
a=V(3,8)
b=V(10,10)
print(a+b)
print(a-b)
print(a==b)