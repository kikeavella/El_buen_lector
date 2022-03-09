class Person:

    __name:str
    __lastName:str
    __contactNumber:int
    __mail:str
    __age:int

    def __init__(self, name:str, lastName:str, contactNumber:int, mail:str, age:int):
        """It is a constructor method for Person"""
        self.__name = name
        self.__lastName = lastName
        self.__contactNumber = contactNumber
        self.__mail = mail
        self.__age = age

    def Get_in(self):
        """It is a method to represents the action of the person entering the bookstore """
        print("The person entering the bookstore")

    def Get_out(self):
        """It is a method to represents the action of the person leaving the bookstore """
        print("The person leaving the bookstore")