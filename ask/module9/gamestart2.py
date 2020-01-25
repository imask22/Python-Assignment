import deck2 as dp
nm=int(input("Enter number of players : "))
listnm=[]
listplayer=[]
listobj=[]

listobj=dp.my_helper()
#print(listobj)
obj23=dp.Deck(listobj)
objhand=dp.hand(obj23)
for i in range(nm):
    ask=input("Enter Player name = ")
    listnm.append(ask)
for k in listnm:
    obj=dp.Player(k,objhand,listobj)
    listplayer.append(obj)
    
obj1=dp.Game()
obj1.getplayer(listplayer,listnm)
    
cont=0
while(True):
    ask=obj1.startplay(listnm)
    if(ask==0):
        print(obj1.displayObj())
        print("You won!")
        break
    
    
