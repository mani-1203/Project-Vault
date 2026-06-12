class Bank_Account:
    def __init__(self,Account_Number):
        self.Account_Number = Account_Number
        self.__Balance=0
    def deposit(self,Amount):
        if Amount <= 0:
            print("Value has to be larger than Zero")
        else:
            self.__Balance += Amount
        return self.__Balance
    def Withdraw(self,Amount):
        if self.__Balance <= 0:
            print("No balance in the account")
        else:
            self.__Balance -= Amount
        return self.__Balance
# acc=Bank_Account('41289189662')
# print(acc.deposit(2000))
# print(acc.Withdraw(500))


class Employee:
    def __init__(self,name):
        self.name=name
        self.__salary=20000
    def get_m(self):
        print(f'{self.name} is viwed his salary')
        # return self.__salary
    def set_m(self,new_salary):
        if new_salary > self.__salary:
            self.__salary=new_salary
            return self.__salary
        else:
            return 'low salary than last one'
# e1=Employee('Mani')
# e1.get_m()
# print(e1.set_m(25000))

class ATM:
    def __init__(self):
        self.__amount=35000
    def get(self,pin):
        if pin == '120312':
            return self.__amount
        else:
            return 'Invalid Pin'
    def set(self,pin,new_amount):
        if pin=='120312':
            if new_amount > 0:
                self.__amount += new_amount
                return f'Your account balance is {self.__amount}'
            else:
                return 'Invalid Amount Input'
        else:
            return "Invalid Pin"
# a=ATM()
# print(a.get('120312'))
# print(a.set('120312',10000))

class Securefile:
    def read(self,password):
        if password == 'Mr@120312':
            print("Access is granted")
        else:
            print("Invalid User")
# s=Securefile()
# s.read('Mr@120312')

class Student:
    def __init__(self,name):
        self.name=name
        self.__marks=0
    def marks(self,marks):
        if 0 <= marks <=100:
            self.__marks=marks
            return self.__marks
        return 'Invalid marks'
    def get_m(self):
        return self.__marks
# s=Student("mani")
# print(s.marks(80))
# print(s.get_m())

class Product:
    def __init__(self,name):
        self.name=name
        self.__price=100
    def discount(self,percentage):
        percentage=percentage/100
        if percentage > 0.7:
            print("Out of range")
        else:
            self.__final_price=self.__price - (self.__price*percentage)
            return self.__final_price
    @property
    def get_m(self):
        return f'The price of the product after discount is {self.__final_price}'
# p=Product("AMWAY")
# p.discount(30)
# print(p.get_m)


class Character:
    def __init__(self,name):
        self.name=name
        self._health=100
    def damage(self,points):
        self.max_limit=200
        if points>self._health:
            return f'{self.name} has health of {self._health} cannot hit more than that'
        elif points<=0:
            return 'Damage is lower'
        else:
            self._health-=points
            return f'{self.name} if left with "{self._health}" health after taking damage {points}'
    def heal(self,points):
        if points>=self.max_limit:
            return f'Cannot heal more than {self.max_limit}'
        else:
            self._health+=points
            if self._health>self.max_limit:
                return f'{self.name} health is reaching more than {self.max_limit}, can not heal '
            return f'After healing {self.name} has {self._health} health.'
    @property
    def get_m(self):
        return self._health
c=Character('mani')
print(c.damage(50))
print(c.heal(180))

class ShoppingCart:
    def __init__(self):
        self.__items=[]
    def add_items(self,items):
        self.__items.append(items)
    def remove(self,items):
        if items in self.__items:
            self.__items.remove(items)
        else:
            print(items,'is not in the list')
    def get_m(self):
        return self.__items.copy()
# s=ShoppingCart()
# s.add_items("phone")
# s.add_items('laptop')
# s.add_items('keys')
#
# s.remove('phone')
#
# print(s.get_m())

class Engine:
    def __init__(self):
        self.__temperature=90
    def get_m(self):
        return f'{self.__temperature} is the current engine temperature'
class Car(Engine):
    def nothing(self):
        pass
        super().get_m()

# e=Engine()
# print(e.get_m())
# c=Car()
# print(c.get_m())

