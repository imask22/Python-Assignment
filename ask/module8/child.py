from automobile import Automobile
class Car(Automobile):
    def __init__(self,make,model,mileage,price,door):
        Automobile.__init__(self,make,model,mileage,price)
        self.make=make
        self.model=model
        self.mileage=mileage
        self.price=price
        self.door=door
    def set_doors(self,door):
        self.door=door
    def get_door(self,door):
        return self.door
    def __str__(self):
        return "Make : "+self.make+" ,Model : "+self.model+" ,Mileage : "+self.mileage+" ,Price : "+self.price+" ,Doors : "+self.door
    
obj=Car("ask","tesla","24","240000","2")
print(obj)        
