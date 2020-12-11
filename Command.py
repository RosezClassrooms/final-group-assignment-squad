from abc import ABC, abstractmethod
#A generic example would be you ordering coffee at coffeeshop.


#receiver ---
#Knows how to execute the command
class Barista:

    def makeCappucino(self):
        print("Barista is making your Cappucino!")

    def makeIceLatte(self):
        print("Barista is making your Ice Latte!")


    def makeBlackCoffee(self):
        print("Barista is making your Black Coffee!")


#------------------------------------------------------------------------------------

#command interface ------ order
#abstract base command class
#declares the interface for executing an operation
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


#----------------------------------------------------------------------

#concrete command classes ------ order
#defines the binding between the Receiver and the action to execute
#invokes methods on the Receiver to fulfill the request

class CappucinoOrderCommand(Command):


    def __init__(self, barista, drink):
        self.drink=drink
        self.barista=barista

    def execute(self):
        if((self.barista is not None and self.drink=="Cappucino")):
            return self.barista.makeCappucino()

    def __str__(self):
        return f'{self.drink} is ready, Enjoy it!'



class IceLatteOrderCommand(Command):

    def __init__(self, barista, drink):
        self.drink=drink
        self.barista=barista

    def execute(self):
        if((self.barista is not None and self.drink=="IceLatte")):
            return self.barista.makeIceLatte()

    def __str__(self):
        return f'{self.drink} is ready, Enjoy it!.'


class BlackCoffeeOrderCommand(Command):
    def __init__(self, barista, drink):
        self.drink=drink
        self.barista=barista

    def execute(self):
        if((self.barista is not None and self.drink=="BlackCoffee")):
            return self.barista.makeBlackCoffee()

    def __str__(self):
        return f'{self.drink} is ready, Enjoy it!'


#--------------------------------------------------------------------------------------
#invoker --------waiter
#issues the request to execute the command

class Waiter:

    def __init__(self, name):
        self.name = name
        self.order = None

    def receiveOrder(self, order):

        self.order = order
        print (f'Waiter {self.name} : I took your order')



    def placeOrder(self):
        coffee = self.order.execute()
        print (f'Waiter {self.name} : Your {self.order}')



#client
#creates the Concrete Command and sets its Receiver
class Customer:
    def __init__(self, name):
        self.name=name
        self.barista=Barista()

    def __str__(self):
        return f'\nCustomer {self.name} wants to order some coffee for her friends.\n'

    def request_cappucino(self, drink):
        return CappucinoOrderCommand(self.barista, drink)

    def request_icelatte(self, drink):
        return IceLatteOrderCommand(self.barista, drink)

    def request_blackcoffee(self, drink):
        return BlackCoffeeOrderCommand(self.barista, drink)






def main():
    waiter=Waiter("Rachel")
    customer=Customer("Monica")
    print(customer)
    request1=customer.request_cappucino("Cappucino")
    waiter.receiveOrder(request1)
    waiter.placeOrder()
    print()

    request2=customer.request_icelatte("IceLatte")
    waiter.receiveOrder(request2)
    waiter.placeOrder()
    print()

    request3=customer.request_blackcoffee("BlackCoffee")
    waiter.receiveOrder(request3)
    waiter.placeOrder()
    print()


if __name__ == "__main__":
    main()
