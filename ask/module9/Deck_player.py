import random
class Card:
    def __init__(self,face,suite,value):
        self.face=face
        self.suite=suite
        self.value=value
    def __str__(self):
        return "Suite : "+self.suite+" : withvalue : "+str(self.value)+" : Face : "+self.face    

        

class Deck:             #cardobj 
    def __init__(self,obj):
        self.listobj=obj

    def Shuffel(self):
        random.shuffle(self.listobj)

    def next_card(self):
        return self.listobj.pop(0),self.listobj.pop(0)
    def one_card(self):
        return self.listobj.pop(0)

    def returns_Cards(self):
        return self.listobj
        
class hand():
    def __init__(self,obj):
        self.obj=obj
        self.drawn=0
        self.card=0
        
    
    def draw_from(self):
        self.obj.Shuffel()
        x,y=self.obj.next_card()
        return x,y
    def drawSingle(self):
        return self.obj.one_card()
        
        

    def return_to(self,card):
        pass


class Player:
    def __init__(self,name):
        self.name=name
        self.sum1=0
    def play(self):
        play=input("Do you wnt to play ?")
        if(play=="yes"):
            self.sum1=main()
            return True
        else:
            return False
            
    def show_hand(self):
        print("Hi "+self.name+"Your sum is = ",self.sum1)


def my_helper():
    listobj=[]
    listface=["A","K","Q","J"]
    listval=[1,13,12,11]
    listSuite=["Hearts","Spade","Diamond","Club"]

    for i in listSuite:
        count=0
        for j in listface:
            obj=Card(j,i,listval[count])
            listobj.append(obj.__str__())
            count+=1
        for p in range(2,11):
            obj=Card("none",i,p)
            listobj.append(obj.__str__())
    return listobj
    
def main():
    listobj=my_helper()
    
    listas=[]

    obj=Deck(listobj)
    count=0
    listcurr=[]
    getsum=0
    obj2=hand(obj)
    var=""


    while(getsum<=45):
        if count==0:
            x,y=obj2.draw_from()
            print(x)
            print(y)
            x=x.split(" : ")
            y=y.split(" : ")
            for val in x:
                if not val.isalpha():
                    getsum+=int(val)
                    #print(val)
                    break
            #print(getsum)
        
            count+=1
            for val in y:
                if not val.isalpha():
                    getsum+=int(val)
                    #print(val)
                    break
            #print(getsum)
        else:
        
            x=obj2.drawSingle()
            print(x)
            x=x.split(" : ")
            for val in x:
                if not val.isalpha():
                    getsum+=int(val)
                    break
            count+=1
    return count
        
        
    

