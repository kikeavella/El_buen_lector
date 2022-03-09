from Person import Person

class Administrator(Person):

    __name:str
    __lastName:str
    __contactNumber:int
    __mail:str
    __age:int

    def __init__(self, name:str, lastName:str, contactNumber:int, mail:str, age:int):
        """It is a constructor method for Administrator"""
        self.__name = name
        self.__lastName = lastName
        self.__contactNumber = contactNumber
        self.__mail = mail
        self.__age = age

    def Get_in(self):
        """Represents the action of the administrator when entering the library"""
        print("Rhe action of the administrator when entering the library")

    def Get_out(self):
        """Represents the administrator's action when exiting the library"""
        print("The administrator's action when exiting the library")

    def Request_report(self):
        """Represents the administrator requesting a report from the employee"""
        print("The administrator requesting a report from the employee")