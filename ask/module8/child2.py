from automobile import Automobile
class Suv(Automobile):
    def __init__(self,make,model,mileage,price,pass_cap):
        Automobile.__init__(self,make,model,mileage,price)
        self.make=make
        self.model=model
        self.mileage=mileage
        self.price=price
        self.door=door
    def set_pass_cap(self,door):
        self.pass_cap=pass_cap
    def get_door(self,door):
        return self.pass_cap
    def __str__(self):
        return "Make : "+self.make+" ,Model : "+self.model+" ,Mileage : "+self.mileage+" ,price : "+self.price+" ,Pass_cap"+self.pass_cap
    
obj=Car("ask","tesla","24","240000","2")
print(obj) 
