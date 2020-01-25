n=int(input("Enter order for magic square"))
mgsqr=[];count=0;sum2=0;sum3=0;sum4=0
list2=n
while(n):
    lst=list(map(int,input().split()))
    mgsqr.append(lst)
    n-=1
sum1=sum(mgsqr[0])
for i in range(len(mgsqr)):
    if(sum(mgsqr[i])!=sum1):
        print("no not a magic square")
        break
    for j in range(len(mgsqr)):
        sum2+=mgsqr[j][i]
        if(i==j):
            sum3+=mgsqr[i][j]
    if(sum2!=sum1):
        print("no, not a magic square")
        break
    sum4+=mgsqr[list2-1-i][i]
    sum2=0
if(sum3==sum1 and sum4==sum1):
    print("yes, magic square")
else:
    print("no,not a magic sq")   

    
    
