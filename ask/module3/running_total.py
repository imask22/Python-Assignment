x,y=7,3
list1=[2,1,3,5,0,1,4]
steps=int((3/0.5)/2)
listsum=[]
for i in range(0,len(list1)):
    sum1=0
    j=i
    for ask in range(0,y):
        
        if j > len(list1):
            j=0
        sum1=sum1+list1[j]
    listsum.append(sum1)

print(max(listsum))
    
    

    
    
    
