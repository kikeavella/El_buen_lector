from Element import Element

class Book:

    __nameElement:str
    __genderElement:str
    __authorElement:str
    __releasEyearElement:int
    __priceElement:float
    __conditionElement:str

    def __init__(self, nameElement:str, genderElement:str, authorElement:str, releasEyearElement:int, priceElement:float, conditionElement:str):
        """It is a constructor method for Book"""
        self.__nameElement = nameElement
        self.__genderElement = genderElement
        self.__authorElement = authorElement
        self.__releasEyearElement = releasEyearElement
        self.__priceElement = priceElement
        self.__conditionElement = conditionElement

    def Be_sold(self):
        """Represents the Book being sold to a customer"""
        print("The Book being sold to a customer")

    def Be_borrowed(self):
        """Represents the Book being loaned to a customer"""
        print("The Book being loaned to a customer")
