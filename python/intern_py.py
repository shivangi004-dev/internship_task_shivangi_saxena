# 1. Employee Management System
########################################################################################################################################

class Employee():
    def __init__(self, name,salary,department):
       self.name= name
       self.salary= salary
       self.department= department
       
    def getDetails(self):
        print("--------------")
        print("employee class ")
        print("--------------")
        return f"name:{self.name}\nsalary:{self.salary}\ndepartment:{self.department}"
        
class Manager(Employee):
    def __init__(self,name,salary,department,teamsize):
        super().__init__(name,salary,department)
        self.teamsize=teamsize
    
    def getDetails(self):
        print("--------------")
        print("manager class ")
        print("--------------")
        return f"name:{self.name} \nsalary:{self.salary} \ndepartment:{self.department} \nteamsize:{self.teamsize}"
    
class Intern(Manager):
    def __init__(self,name,salary,department,teamsize,duration):
        super().__init__(name,salary,department,teamsize)
        self.duration= duration
        
    def getDetails(self):
        print("--------------")
        print("intern class ")
        print("--------------")
        return f"name:{self.name} \nsalary:{self.salary} \ndepartment:{self.department} \nteamsize:{self.teamsize} \nduration:{self.duration} months"

Emp = Employee("Alice", 4000, "HR")
print(Emp.getDetails()) 

Man = Manager("Bob", 8000, "Sales", 10)
print(Man.getDetails())

Int= Intern("Aditi",2000,"CS",2,6)
print(Int.getDetails())

######################################################################################################################################################

# 2. Library System - Class and Constructor 

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f'Reading "{self.title}" by {self.author}.'

    def get_summary(self):
        return f'"{self.title}" by {self.author} has {self.pages} pages.'
    
book = Book("1984", "George Orwell", 328)
print("-----------------------------------")
print(" Library System ")
print("-----------------------------------")
print(book.read())
print(book.get_summary())
print("-----------------------------------")


######################################################################################################################################################

# 3. Online Payment System
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def process_payment(self,amount):
        pass
    
class CreditCard(PaymentMethod):
    def __init__(self,card_number,balance):
        self.card_number=card_number
        self.balance=balance
        
    def authenticate(self):
        if len(self.card_number)==16 and self.card_number.isdigit():
            print("credit card : authentication successful")
            return True
        else:
            print("credit card : authentication fail")
            return False
    
    def process_payment(self, amount):
        if self.authenticate():
            if amount<=self.balance:
                self.balance -= amount
                print(f"credit card : payment of {amount} processed. \nRemaining balance: {self.balance}")
            else:
                print("Credit Card: Do not have enough funds.")
        else:
            print("Credit Card: Payment failed due to authentication faliure.")
class PayPal(PaymentMethod):
    def __init__(self,account_email,balance):
        self.account_email=account_email
        self.balance=balance
    
    def authenticate(self):
        if "@" in self.account_email:
            print("PayPal: Authentication successful")  
            return True
        else:
            print("PayPal: Authentication failed")
            return False
    
    def process_payment(self, amount):
        if self.authenticate():
            if amount<=self.balance:
                self.balance -= amount
                print(f"PayPal : payment of {amount} processed. \nRemaining balance: {self.balance}")
            else:
                print("PayPal: Do not have enough funds.")
        else:
            print("PayPal: Payment failed due to authentication faliure.") 
        
class Bitcoin(PaymentMethod):
    def __init__(self, wallet_address, balance):
        self.wallet_address = wallet_address
        self.balance = balance
        
    def authenticate(self):
        if len(self.wallet_address) == 34:
            print("Bitcoin: Authentication successful")
            return True
        else:
            print("Bitcoin: Authentication failed")
            return False
    
    def process_payment(self, amount):
        if self.authenticate():
            if amount<=self.balance:
                self.balance -= amount
                print(f"Bitcoin : payment of {amount} processed. \nRemaining balance: {self.balance}")
            else:
                print("Bitcoin: Do not have enough funds.")
        else:
            print("Bitcoin: Payment failed due to authentication faliure.")
            
credit_card = CreditCard("8769856473425471", 10000)
paypal = PayPal("abc@abc.com", 5000)
bitcoin = Bitcoin("ASFjhsgdf43SHJFhgff345gthg4fswlkup", 10)

print("********************** ")
print("Credit card receipt ")
print("********************** \n")

credit_card.process_payment(4000)

print("********************** ")
print("PayPal receipt ")
print("**********************")

paypal.process_payment(1000)

print("**********************")
print("Bitcoin receipt ")
print("********************** ")

bitcoin.process_payment(5)

######################################################################################################################################################