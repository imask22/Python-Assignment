list1=[0,0,0,0,0,0,0,0,0]
list2=["","","","","","","","",""]

listask=[]
def create_list(i):
    if(i=="a"):
        listnow=[[" ","*"," "],["*","*","*"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="b"):
        listnow=[["*","*","*"],["*","*"," "],["*","*","*"]]
        listask.append(listnow)
    if(i=="c"):
        listnow=[["*","*","*"],["*"," "," "],["*","*","*"]]
        listask.append(listnow)
    if(i=="d"):
        listnow=[["*","*"," "],["*"," ","*"],["*","*"," "]]
        listask.append(listnow)
    if(i=="e"):
        listnow=[["*","*","*"],["*","*"," "],["*","*","*"]]
        listask.append(listnow)
    if(i=="f"):
        listnow=[["*","*","*"],["*","*",""],["*"," "," "]]
        listask.append(listnow)
    if(i=="g"):
        listnow=[["*","*","*"],["*","*","*"],["*","*","*"]]
        listask.append(listnow)
    if(i=="h"):
        listnow=[["*"," ","*"],["*","*","*"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="i"):
        listnow=[["*","*","*"],[" ","*"," "],["*","*","*"]]
        listask.append(listnow)
    if(i=="j"):
        listnow=[["*","*","*"],[" ","*"," "],["*","*"," "]]
        listask.append(listnow)
    if(i=="k"):
        listnow=[["*","*"," "],["*"," "," "],["*","*"," "]]
        listask.append(listnow)
    if(i=="l"):
        listnow=[["*"," "," "],["*"," "," "],["*","*","*"]]
        listask.append(listnow)
    if(i=="m"):
        listnow=[["*"," ","*"],["*","*"," *"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="n"):
        listnow=[["*","","*"],["*","*","*"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="o"):
        listnow=[["*","*","*"],["*"," ","*"],["*","*","*"]]
        listask.append(listnow)
    if(i=="p"):
        listnow=[["*","*","*"],["*","*","*"],["*"," "," "]]
        listask.append(listnow)
    if(i=="q"):
        listnow=[["*","*","*"],["*","*","*"],["*","*","*"]]
        listask.append(listnow)
    if(i=="r"):
        listnow=[["*","*","*"],["*","*","*"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="s"):
        listnow=[["*","*","*"],["*","*","*"],["*","*","*"]]
        listask.append(listnow)
    if(i=="t"):
        listnow=[["*","*","*"],[" ","*"," "],[" ","*"," "]]
        listask.append(listnow)
    if(i=="u"):
        listnow=[["*"," ","*"],["*"," ","*"],["*","*","*"]]
        listask.append(listnow)
    if(i=="v"):
        listnow=[["*"," ","*"],[" "," "," "],[" ","*"," "]]
        listask.append(listnow)
    if(i=="w"):
        listnow=[["*"," ","*"],["*","*","*"],["*"," ","*"]]
        listask.append(listnow)
    if(i=="x"):
        listnow=[["*"," ","*"],[" ","*"," "],["*"," ","*"]]
        listask.append(listnow)
    if(i=="y"):
        listnow=[["*"," ","*"],[" ","*"," "],[" ","*"," "]]
        listask.append(listnow)
    if(i=="z"):
        listnow=[["*","*","*"],["*","*","*"],["*","*","*"]]
        listask.append(listnow)
    
str1=input()
list1=[str(x) for x in str1]
for ask in list1:
    create_list(ask)
for list2 in listask:
    print(" ".join(list2[0]),end="  ")
print("")
for list2 in listask:
    print(" ".join(list2[1]),end="  ")
print("")
for list2 in listask:
    print(" ".join(list2[2]),end="  ")
