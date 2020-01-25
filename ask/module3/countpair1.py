list1=[int(x) for x in input().split(" ")]
list2=[]
for i in range(0,max(list1)+1):
    list2.append(0)
sum1=int(input("Enter sum : "))
for i in range(0,len(list1)):
    list2[list1[i]]=i

for i in range(0,len(list1)):
    if(list2[sum1-list1[i]] != i):
        if(list2[sum1 - list1[i]] !=0):
            print(i," ",list2[sum1 - list1[i]])
