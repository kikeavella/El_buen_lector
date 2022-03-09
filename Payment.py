from datetime import time
from datetime import date
from Client import Client

class Payment(Client):

    __name:str
    __lastName:str
    __shape:str
    __value:float
    __hour:time
    __date:date
    __cardExpirationDate:date
    __cardDigitLength:int
    __cardPrefix:int
    __cardCharacters:int
    __affiliate:bool
    __place:str

    def __init__(self, name:str, lastName:str, shape:str, value:float, hour:time, date:date, cardExpirationDate:date, cardDigitLength:int, cardPrefix:int, cardCharacters:int, affiliate:bool, place:str):
        """It is a constructor method for Payment"""
        self.__name = name
        self.__lastName = lastName
        self.__shape = shape
        self.__value = value 
        self.__hour = hour
        self.__date = date
        self.__cardExpirationDate = cardExpirationDate
        self.__cardDigitLength = cardDigitLength
        self.__cardPrefix = cardPrefix
        self.__cardCharacters = cardCharacters
        self.__affiliate = affiliate
        self.__place = place

    def Pay(self):
        """Represents the transaction that the client makes to the bookstore"""
        if self.__value > 0:
            if self.__shape == "cash":
                if self.__affiliate == 1:
                    print("The discount transaction that {self.__name} {self.__lastName} makes to the bookstore {self.__place}, was on the day {self.__date} with the hour {self.__hour}.")
                else:
                    print("The transaction without discount that {self.__name} {self.__lastName} makes to the bookstore {self.__place}, was on the day {self.__date} with the hour {self.__hour}.")
            if self.__shape == "credit card":
                if self.__cardExpirationDate > self.__date:
                    if self.__cardDigitLength == 13:
                        if self.__cardPrefix == 4:
                            if int(len(str(self.__cardCharacters))) >= 0 and int(len(str(self.__cardCharacters))) <= 9:
                                if self.__affiliate == 1:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Visa credit card, has a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour}.")
                                else:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Visa credit card, does not have a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour }.")
                            else:
                                print("The credit card does not have the allowed characters")
                        else:
                            print("The credit card does not have the allowed prefixes")
                    if self.__cardDigitLength == 16:
                        if self.__cardPrefix >= 51 and self.__cardPrefix <= 59:
                            if int(len(str(self.__cardCharacters))) >= 0 and int(len(str(self.__cardCharacters))) <= 9:
                                if self.__affiliate == 1:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Master credit card, has a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour}.")
                                else:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Master credit card, does not have a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour }.")
                            else:
                                print("The credit card does not have the allowed characters")
                        else:
                            print("The credit card does not have the allowed prefixes")
                    if self.__cardDigitLength == 14:
                        if self.__cardPrefix == 30 or self.__cardPrefix == 36 or self.__cardPrefix == 38:
                            if int(len(str(self.__cardCharacters))) >= 0 and int(len(str(self.__cardCharacters))) <= 9:
                                if self.__affiliate == 1:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Diners Club credit card, has a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour}.")
                                else:
                                    print("The transaction made by {self.__name} {self.__lastName} with the Diners Club credit card, does not have a discount, is made to the bookstore {self.__place}, on the day {self.__date} with the hour {self.__hour }.")
                            else:
                                print("The credit card does not have the allowed characters")
                        else:
                            print("The credit card does not have the allowed prefixes")
                    else:
                        print("The credit card does not have the length of digits allowed")
                else:
                    print("The credit card is expired")
            else:
                print("Your payment method is not valid")
        else:
            print("The transaction could not be done due to lack of money")
