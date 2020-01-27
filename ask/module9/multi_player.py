import card_game_multi_player as dp
obj1=dp.Game()
def start(listplayer,listnm):
    global obj1
    obj1=dp.Game()
    obj1.getplayer(listplayer,listnm)
    return obj1
    

def play1(listnm):
    nm=int(input("Enter number of players : "))
    for i in range(nm):
        ask=input("Enter Player name = ")
        listnm.append(ask)
    for k in listnm:
        obj=dp.Player(k,objhand,listobj)
        listplayer.append(obj)

    while(True):
        ask=obj1.startplay(listnm)
        if(ask=="off"):
            print("You won!")
            break
while(True):
    try:
        listnm=[]
        listplayer=[]
        listobj=[]

        listobj=dp.my_helper()
        obj23=dp.Deck(listobj)
        objhand=dp.hand(obj23)
        print("Can you Score > 30 ?? fastest and luckiest will win challenge ")
        print("1 to play game")
        print("2 to show all scroes so far")
        n=int(input())
        if(n==1):
            obj1=start(listplayer,listnm)
            play1(listnm)
        elif(n==2):
            obj1.Displayall()
    except:
        print("Deck emptied Game Ties")
        
