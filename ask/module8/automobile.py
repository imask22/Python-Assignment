class Automobile:
    def __init__(self,make,model,mileage,price):
        self.__make=make
        self.__model=model
        self.__mileage=mileage
        self.__price=price
    def set_make(self,make):
        self.__make=make
    def set_model(self,model):
        self.__model=model
    def set_mileage(self,model):
        self.__mileage=mileage
    def set_price(self,price):
        self.__price=price
    def get_make(self,make):
        return self.make
    def get_model(self,model):
        return self.model
    def get_mileage(self,mileage):
        return self.mileage
    def get_price(self,price):
        return self.price
    
    
    
