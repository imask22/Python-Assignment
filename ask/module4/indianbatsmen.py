n=int(input("Enter no of batsman : "))
dict1={}
Type_of_player=str(input("Type of player : "))
dict1[Type_of_player]={}
list2=[]
while(n):
    Name_of_player=str(input("Name of Player : "))
    dict1[Type_of_player][Name_of_player]={}
    
    Matches=input("Matches : ")
    Runs=input("Runs : ")
    Average=input("Average : ")
    Highest_Score=int(input("Highest_score : "))
    
    dict1[Type_of_player][Name_of_player]['Matches']=Matches
    dict1[Type_of_player][Name_of_player]['Runs']=Runs
    dict1[Type_of_player][Name_of_player]['Average']=Average
    dict1[Type_of_player][Name_of_player]['Highest Score']=Highest_Score
    list2.append([Type_of_player,Name_of_player,Matches,Runs,Average,Highest_Score])
    n=n-1

count=0
max1=0
thisc=0
for i in list2:
    if max1<=i[5]:
        max1=i[5]
        thisc=int(count)
    count+=1
#prints highest batsman detail
print(dict1[Type_of_player][list2[thisc][1]]) 
