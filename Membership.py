class Membership:

    __duration:str

    def __init__(self, duration:str):
        """It is a constructor method for Membership"""
        self.__duration = duration 

    def Be_sold(self):
        """Represents the membership being sold to a customer"""
        print("The membership being sold to a customer")