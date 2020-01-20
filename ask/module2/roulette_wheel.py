n=int(input("Enter a pocket number : "))
if(n<0 or n>36):
    print("error")
elif n==0:
    print("green")    
elif n>=1 and n<=10:
    if(n%2==0):
        print("black")
    else:
        print("red")
elif(n>=11 and n<=18):
    if(n%2==0):
        print("red")
    else:
        print("black")    
elif(n>=19 and n<=28):
    if(n%2==0):
        print("black")
    else:
        print("red")
else:
    if(n%2==0):
        print("red")
    else:
        print("black")
    
