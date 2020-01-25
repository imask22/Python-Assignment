siz=int(input())


mid=siz-1
siz=siz*2

for i in range(0,siz+1):
    if(i==siz/2-1):
        print("*"*(siz//2-i),end="")
    elif(i<siz/2):
        print("*"*(siz//2-i))
    
    else:
        print("*"*(i-siz//2))



for i in range(0,siz-1,2):
    print(" "*((siz-i+1)-1),end="")
    print("* "*(i-1),end="")
    print("")

for i in range(0,siz,2):
    print(" "*(i),end="")
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
    print(" "*((siz-i)-1),end="")
    for j in range(0,i):
        if(j==0 or j==i-1):
            print("* ",end="")
        elif(i==siz-1):
            print("* ",end="")
        else:
            print("  ",end="")
    print("")






    
    
