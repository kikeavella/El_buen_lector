from Person import Person

class Employee(Person):

    __name:str
    __lastname:str
    __contactnumber:int
    __mail:str
    __age:int

    def __init__(self, name:str, lastname:str, contactnumber:int, mail:str, age:int):
        """It is a constructor method for Employee"""
        self.__name = name
        self.__lastname = lastname
        self.__contactnumber = contactnumber
        self.__mail = mail
        self.__age = age

    def Get_in(self):
        """It is a method to represents the action of the employee entering the bookstore"""
        print("The employee entering the bookstore")

    def Get_out(self):
        """It is a method to represents the action of the employee leaving the bookstore"""
        print("The employee leaving the bookstore")

    def Register_client(self):
        """Represents the employee registering a client with their data in the bookstore database"""
        print("The employee registering a client with their data in the bookstore database")

    def Update_client(self):
        """Represents the employee updating the data of a client, except the affiliation, in the library database"""
        print("Represents the employee updating the data of a client, except the affiliation, in the library database")

    def Delete_client(self):
        """Represents the employee deleting the data of a client in the library database"""
        print("The employee deleting the data of a client in the library database")

    def Sell_affiliation(self):
        """Represents the employee by registering the type of affiliation that a customer bought for the first time in the bookstore database"""
        print("The employee by registering the type of affiliation that a customer bought for the first time in the bookstore database")

    def Renew_membership(self):
        """Represents the employee by registering the type of affiliation that a client renewed in the bookstore database"""
        print("The employee by registering the type of affiliation that a client renewed in the bookstore database")

    def Generate_report(self):
        """Represents the employee generating a useful report for the administrator"""
        print("The employee generating a useful report for the administrator")

    def Enter_item(self):
        """Represents the employee entering into the library database an item that entered the inventory to be active"""
        print("The employee entering into the library database an item that entered the inventory to be active")

    def Lower_item(self):
        """Represents the employee removing an inventory item from the library database so that it no longer appears active"""
        print("The employee removing an inventory item from the library database so that it no longer appears active")

    def Sell(self):
        """Represents the employee recording data of the sale of an item of active inventory "time, date, place, customer and other" in the database of the bookstore"""
        print("Represents the employee recording data of the sale of an item of active inventory time, date, place, customer and other in the database of the bookstore")

    def Lend(self):
        """Represents the employee recording data of a loan of an item of active inventory "time, date, place, client and other" in the database of the bookstore"""
        print("The employee recording data of a loan of an item of active inventory time, date, place, client and other in the database of the bookstore")

    def Request_transaction(self):
        """Represents the employee registering data of the transaction through which an affiliation, a sale, a loan of an active element of the inventory is being made, such as the form of payment of the client "cash, card" visa, mastercard and diners club "", value, date, time"""
        print("The employee registering data of the transaction through which an affiliation, a sale, a loan of an active element of the inventory is being made, such as the form of payment of the client ""cash, card"" visa, mastercard and diners club "", value, date, time")

    def Update_item_data(self):
        """Represents the employee updating basic data and the status of an active inventory item in the library database"""
        print("The employee updating basic data and the status of an active inventory item in the library database")

    def Sort_out(self):
        """Represents the employee sorting an item from active inventory alphabetically in the bookstore"""
        print("The employee sorting an item from active inventory alphabetically in the bookstore")

    def Check_in_system(self):
        """Search the bookstore system for an item that may be active, per customer request"""
        print("The bookstore system for an item that may be active, per customer request")

    def Consult_physically(self):
        """Physically search the library for an item that may be active, per customer request"""
        print("Physically search the library for an item that may be active, per customer request")


