class AgeError(Exception):
    pass
class Person:
    def __init__(self, age):
        if age < 18:
            raise AgeError("Age must be 18 or above")
        else:
            self.age = age
            print("Valid age, object created")
# try:
#     p = Person(1)
#     print(p.age)
# except AgeError as e:
#     print(e)
# finally:
#     print('Code executed.')


class Invalid_Age_Error(Exception):
    pass
class Bank_Account:
    def __init__(self,name,age,pancard):
        self.name=name
        self.pancard=pancard
        if age<18:
            raise Invalid_Age_Error('Age should be greater than 18')
        else:
            self.age=age
            print(self.name,'is',self.age,"is greater than 18.")
# try:
#     b=Bank_Account('Mani',2,'JMCPM8439N')
# except Invalid_Age_Error as I:
#     print(I)
# finally:
#     print("Code Executed.")

class Students:
    def set_marks(self,marks):
        if 0< marks >100:
            raise ValueError(f'marks should in between range of 0 and 100.')
        else:
            marks=marks
            print(marks,'is your score')
# try:
#     s=Students()
#     s.set_marks(900)
# except ValueError as v:
#     print('Error :',v)


class ValidAgeError(Exception):
    pass

class Voter:
    def __init__(self,name):
        self.name=name
    def check_Eligibility(self,age):
        try:
            if age<18:
                raise ValidAgeError(f"{self.name}'s age is lower than 18, not allowed." )
            else:
                age=age
                print(f"{self.name}'s age is {age},greater than 18, allowed to vote.")
        except ValidAgeError as V:
            print("Error :",V)
# v=Voter("Mani")
# v.check_Eligibility(1)


class withdrawError(Exception):
    pass
class Bank:
    def __init__(self,balance):
        self.balance=balance
        print(f"Avaliable balance = {self.balance} in your account.")
    def withdraw(self,amount):
        if amount>self.balance:
            raise withdrawError(f"{amount} is greater than the available balance.")
        else:
            amount = amount
            print(f"{amount} is deducted from balance")
            self.balance -= amount
            print(f"After deduction available balance = {self.balance}.")
# try:
#     b=Bank(25000)
#     b.withdraw(50000)
# except withdrawError as W:
#     print("Error :",W)

class NotImplemented(Exception):
    pass
class Shape:
    def area(self):
        raise NotImplemented('sub class must implement the area method')
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
# try:
#     r=Rectangle(10,10)
#     print('Area of the Rectangle is',r.area())
#     r.area()
# except NotImplemented as N:
#     print("Error:",N)

class InvalidPassword(Exception):
    pass

class LoginSystem:
    def __init__(self,name):
        self.name = name
    def login(self,password):
        try:
            if password == 'Mr@120312':
                print(f'{self.name} you are login is successful')
            else:
                raise InvalidPassword('password is incorrect')
        except InvalidPassword as I:
            print("Error: ",I)
# l=LoginSystem('Mani')
# l.login('Mr@120312')

class NotIterable(Exception):
    pass

def find_length(v):
    c=0
    if isinstance(v,(list,str,tuple,set)):
        for i in v:
            c+=1
        return c
    else:
        raise NotIterable(f'{type(v)} is not Iterable.')
# try:
#     print(find_length('l'))
# except NotIterable as N:
#     print(f"Error: {N}")

class Service:
    def m1(self):
        raise ValueError('There is something wrong in this method.')
    def m2(self):
        try:
            self.m1()
        except ValueError as V:
            print("ERROr:",V)
        finally:
            pass
# s=Service()
# s.m2()
class UserInput:
    def get_integer(self,value):
        try:
            num=int(value)
            print(num)
        except ValueError:
            print("value error")
        except TypeError:
            print("Type Error")
# u=UserInput()
# u.get_integer('552')

class LengthError(Exception):
    pass

class PasswordValidator():
    def validate(self,password):
        try:
            if len(password)<8:
                raise LengthError(f"{password} is shoter.")
            else:
                password=password
                print(f'your {password} is valid.')
        except LengthError as L:
            print("Error:",L)
# p=PasswordValidator()
# p.validate('12031203')

