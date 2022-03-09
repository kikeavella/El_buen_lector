class Element:

    __name:str
    __gender:str
    __author:str
    __releasEyear:int
    __price:float
    __condition:str

    def __init__(self, name:str, gender:str, author:str, releasEyear:int, price:float, condition:str):
        """It is a constructor method for Element"""
        self.__name = name
        self.__gender = gender
        self.__author = author
        self.__releasEyear = releasEyear
        self.__price = price
        self.__condition = condition

    def Be_sold(self):
        """Represents the element being sold to a customer"""
        print("The element being sold to a customer")

    def Be_borrowed(self):
        """Represents the element being loaned to a customer"""
        print("The element being loaned to a customer")
