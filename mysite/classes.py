class User:

    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

#method
    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1

class Customer(User):

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

#init user object

timothy = User('Timothy kayode', 'tobytimoty@gmail.com', 21)

print(timothy.name)

toby = User('toby oluwasayo', 'toby@timothy.com', 3)


toby.has_birthday()

print(toby.greeting())


#init customer

john = Customer('John Wick', 'johnwick@john.com', '45')

john.set_balance(500)

