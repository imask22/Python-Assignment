n=int(input("Enter number"))
ask = [int(x) for x in str(n)]
for i in range(0,len(ask)):
    if(ask[i]==9):
        ask[i]=0
        continue
    ask[i]+=1
    
result=0
for i in range(0,len(ask)):
    result+=ask[i]
    result=result*10
    
print(int(result/10))
