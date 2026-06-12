# class Students:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks= marks
#     def is_valid(self):
#         if self.marks > 40:
#             return f'{self.name} is passed'
#         else:
#             return f'{self.name} is failed'
# s=Students('Mani',90)
# print(s.is_valid())

class Employees:
    change_comp="net"
    def __init__(self,name):
        self.name = name
    @classmethod
    def change_name(cls,new_name):
        cls.change_comp=new_name
#
# e=Employees("Mani")
# e.change_name("CV")
# print(e.change_comp)

class Even:
    @staticmethod
    def methodOps(a):
        if a%2==0:
            print("Even")
        else:
            print('odd')
# c=Even()
# c.methodOps(2)
# Even.methodOps(3)

class Students:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>self.passing_marks:
            print(f"{self.name} is PASS")
        else:
            print(f"{self.name} is FAIL")
    @classmethod
    def update_passing_marks(cls,new_passing_marks):
        cls.passing_marks=new_passing_marks
    @staticmethod
    def grade(marks):
        if marks>=90:
            print("A")
        elif marks<90 and marks>40:
            print("B")
        else:
            print("F")
# s=Students("Mani",99)
# s.result()
# Students.update_passing_marks(60)
# s.grade(66)

# print(Students.passing_marks)

class Car:
    wheels =4
    def display(self,milage):
        print(f'{milage} km/hr')
        return milage
    @classmethod
    def change_wheels(cls,new_wheels):
        cls.wheels=new_wheels
# c=Car()
# c.display(30)
# c.change_wheels(5)
# print(c.wheels)

class Book:
    t_book=3
    def __init__(self,title,author):
        if Book.is_valid_title(title):
            self.title=title
            self.author=author
            Book.t_book+=1
            self.title=title
        else:
            self.title=title
            print(f'{self.title} is not a valid title.')

    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split()
        return cls(title.strip(),author.strip())

    @staticmethod
    def is_valid_title(title):
        if len(title.strip())>=3:
            return True
        return None
    def display(self):
        print(f'{self.title},{self.author}')
# b1=Book('Python Basics',"gayatri")
# b1.display()
#
# b2=Book.from_string('Java programming mani')
# b2.display()
#
# b3=Book('my','dsjbgksd')
# b3.display()
# print(Book.t_book)

class Employee:
    b_rate =0.1
    def __init__(self,name,base_salary):
        self.name = name
        if Employee.is_valid_salary(base_salary):
            self.salary=base_salary
    def final_salary(self):
        return self.salary+(self.salary*self.b_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.b_rate= new_rate
    @staticmethod
    def is_valid_salary(base_salary):
        return base_salary > 0

# e=Employee("mani",25000)
# # e.is_valid_salary(25000)
# e.update_bonus(0.5)
# print(e.final_salary())
#
# print(e.b_rate)


class Course:
    total_students=5
    def __init__(self,name,age):
        self.name = name
        if Course.is_eligible(age):
            self.age=age
            print(f'{self.name} is eligible to join the course.')
        else:
            print(f'{self.name} is not eligible.')
    def enroll(self):
        if Course.is_eligible(self.age):
            Course.total_students+=1
    @classmethod
    def show_total(cls):
        return cls.total_students
    @staticmethod
    def is_eligible(age):
        return age>18
# c1=Course('mani',20)
# c1.enroll()
# print(c1.show_total())
# c2=Course("gayatri",12)
# print(c2.show_total())
#
# c2.enroll()



class BankAccount:
    bank_name='SBI'
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        if BankAccount.valid_amount(amount):
            self.balance+=amount
            return self.balance
        else:
            return "invalid amount"
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def valid_amount(amount):
        return amount>0

# b=BankAccount('mani',25000)
# print(b.deposit(-10000))
# b.change_bank_name("ICICI")
# print(b.bank_name)

class Library:
    total_books=100
    def __init__(self,name):
        self.name=name
    def borrow(self,taken,pin):
        if Library.is_valid(pin):
            if pin =="12345678912345":
                self.taken=taken
                Library.total_books -= self.taken
                print(f'{self.name} is borrowed {self.taken} books. Remaining books {Library.total_books}.')
    def submit(self,submit,pin):
        if Library.is_valid(pin):
            if pin == "12345678912345":
                self.submit=submit
                Library.total_books += self.submit
                print(f'{self.name} is returned {self.submit} books. Remaining books {Library.total_books}.')
    @staticmethod
    def is_valid(pin):
        if len(pin) > 13:
            return pin
        return None

l=Library("mani")
l.borrow(2,'12345678912345')
l.submit(2,'12345678912345')