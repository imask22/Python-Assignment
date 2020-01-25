siz=int(input())

for i in range(0,siz):
    for h in range(0,siz-i):
        print("*",end="")
    if(i!=siz-1):
        print("")

for i in range(0,siz+1):
    for j in range(0,i):
        print("*",end="")
    print("")





mid=siz-1
siz=siz*2


for i in range(0,siz-1,2):
    for k in range(siz-1-i,-1,-1):
        print(" ",end="")
    for j in range(0,i-1):
        print("* ",end="")
    print("")

for i in range(0,siz,2):
    for k in range(0,i):
        print(" ",end="")
    for j in range(siz-2,i-1,-1):
        print("* ",end="")
    print("")








for i in range(0,siz):
    for j in range(0,siz):
        if(j==mid and i!=mid):
            print("*",end="")
        elif(i==mid):
            print("*",end="")
        else:
            print(" ",end="")
    print("")









for i in range(0,siz):
    for k in range(siz-1-i,-1,-1):
        print(" ",end="")
    for j in range(0,i):
        if(j==0 or j==i-1):
            print("* ",end="")
        elif(i==siz-1):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")








    
    
