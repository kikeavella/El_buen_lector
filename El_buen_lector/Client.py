from Person import Person

class Client(Person):

    __name:str
    __lastName:str
    __contactNumber:int
    __mail:str
    __age:int
    __membership:bool

    def __init__(self, name:str, lastName:str, contactNumber:int, mail:str, age:int, membership:bool):
        """It is a constructor method for Client"""
        self.__name = name
        self.__lastName = lastName
        self.__contactNumber = contactNumber
        self.__mail = mail
        self.__age = age
        self.__membership = membership 
    
    def Get_in(self):
        """Represents the action of the client entering the bookstore"""
        print("The client entering the bookstore")

    def Get_out(self):
        """Represents the action of the client leaving the bookstore"""
        print("The client leaving the bookstore")

    def Borrow(self):
        """Represents the client borrowing a permitted item from the bookstore's inventory"""
        print("The client borrowing a permitted item")

    def Buy_item(self):
        """Represents the client purchasing a permitted item from the bookstore's inventory"""
        print("The client purchasing a permitted item")

    def Buy_membership(self):
        """Represents the client purchasing a type of bookstore membership"""
        print("The client purchasing a type of bookstore membership")

    def Pay(self):
        """Represents the client giving money in cash or in a transaction to the bookstore employee, due to a purchase of a membership, an active item or a loan of an active item"""
        print("The client giving money in cash or in a transaction to the bookstore employee, due to a purchase of a membership, an active item or a loan of an active item")

    def Consult(self):
        """Represents the client asking the employee to find an item that may be active in the library"""
        print("The client asking the employee to find an item that may be active in the library")
