# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#creating a class
class User:
    #constructor a function for instatiating an object from a class
    def __init__(self, name,email,age):
        self.name = name #self is the same as this.
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
#init user object
parth = User('Parth Kharade','email@email.com',21)

print(parth.name,parth.age)
print(parth.greeting())

#extending a class
class Customer(User):
     #constructor a function for instatiating an object from a class
    def __init__(self, name,email,age):
        self.name = name #self is the same as this.
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#init customer

Aishu = Customer('Aishu','Aishu@gmail.com','28')
Aishu.set_balance(5000)
print(Aishu.greeting())
