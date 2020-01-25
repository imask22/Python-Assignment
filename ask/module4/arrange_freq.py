list1=[int(x) for x in input().split()]
listc=[]
for i in list1:
    listc.append([i,list1.count(i)])
listc.sort(reverse=True)
listc.sort(key =  lambda x:x[1])
listc=listc[::-1]
for i in listc:
    print(i[0],end=" ")
    


    


        
        
    
    
