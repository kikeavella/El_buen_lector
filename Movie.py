from Element import Element

class Movie:

    __name:str
    __gender:str
    __author:str
    __releasEyear:int
    __price:float
    __condition:str
    __format:str

    def __init__(self, name:str, gender:str, author:str, releasEyear:int, price:float, condition:str, format:str):
        """It is a constructor method for Movie"""
        self.__name = name
        self.__gender = gender
        self.__author = author
        self.__releasEyear = releasEyear
        self.__price = price
        self.__condition = condition
        self.__format = format

    def Be_sold(self):
        """Represents the movie being sold to a customer"""
        print("The movie being sold to a customer")

    def Be_borrowed(self):
        """Represents the movie being loaned to a customer"""
        print("The movie being loaned to a customer")
