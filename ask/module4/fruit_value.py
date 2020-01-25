#created using try catch
n=int(input("enter number of fruits "))
fruit_list=[]
i=1
dict21=dict()
while(n>0):
    
    d=dict()
    dict21[i]=d
    name = input("Enter Fruit name :  ")
    fruit_list.append(name)
    d1=dict()
    d[name] = d1
    d1['binomial name'] = input('binomial name ')
    print("name of 3 major producers ", end=" ")
    l = []
    l.append(input().split(" "))
    d1['major producer'] = l
    d2=dict()
    d1['nutrients'] = d2
    d2['carbs'] = int(input("carbs"))
    d2['protien'] = int(input("protiens"))
    d2['fat'] = int(input("fat"))
    i+=1
    n-=1
print(dict21)
ask=[]
for x in range(i):
    try:
        ask.append(dict21[x+1][fruit_list[x]]['nutrients']['protien'])
    except KeyError:
    #wont work without it needs try Catch Block
        print("",end="")
for k in range(i):
    try:
        if max(ask)==dict21[k+1][fruit_list[k]]['nutrients']['protien']:
            print(fruit_list[k])
    except KeyError:
        print(" ",end=" ")
