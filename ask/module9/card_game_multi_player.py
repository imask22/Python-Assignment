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
        Shuffel()
        return self.listobj.pop(0),self.listobj.pop(0)

    def one_card(self):
        return self.listobj.pop(0)

    def returns_Cards(self):
        return self.listobj
        
class hand:
    def __init__(self,obj):
        self.obj=obj
        self.drawn=0
        self.card=0
        self.hasdeck=[]
    def draw_from(self):
        self.obj.Shuffel()
        x,y=self.obj.next_card()
        return x,y
    
    def drawSingle(self):
        self.obj.Shuffel()
        return self.obj.one_card()

    def return_to(self,card):
        pass


class Player:
    def __init__(self,name,obj,listobj,credit=0):
        self.name=name
        self.credit=0
        self.sum=0
        self.obj=obj
        self.listobj=listobj
    def play(self):
        self.credit,self.sum=main(self.sum,self.obj,self.listobj,self.credit)

        #self.sum=sum1
        if(self.sum>30):
            return True
            
    def show_hand(self):
        print("Your credit Score is = ",self.credit)
        
    def show_infoScore(self):
        return("Name : "+self.name+"tour Score is : "+str(self.credit))

class Game:
    def __init__(self):
        self.playerinfo=[]
        self.listnm=[]
    def burst_probablity(obj):
        pass
    def getplayer(self,list1,list2):
        self.playerinfo=list1
        self.listnm=list2
    def startplay(self,listnm):
        self.listnm=listnm
        count=0
        for i in self.playerinfo:
            print("Chance of player = " + listnm[count])
            var=i.play()
            if(var):
                print("player "+listnm[count]+" ",end="")
                return "off"
            count=(count+1)%len(listnm)
    def displayObj(self,count):
        print(self.listnm[count]+" won the game congrats|||")

    def Displayall(self):
        for i in self.playerinfo:
            a=i.show_infoScore()
            print(a)

        
        
        


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
    
def main(sum1,obj2,listobj,count1):
    listobj=my_helper()
    
    listas=[]

    
    count=count1
    listcurr=[]
    getsum=sum1
    var=""


    if(getsum<=30):
        x=obj2.drawSingle()
        
        print(x)
        x=x.split(" : ")
        for val in x:
            if not val.isalpha():
                getsum+=int(val)
                break
        count+=1
        
        return getsum,getsum
        
