list1=[int(x) for x in input().split(" ")]
list2=[int(x) for x in input().split(" ")]
list3pair=[]
sum1=int(input("Enter sum :"))
for i in list1:
    for j in list2:
        if(i+j==sum1):
            list3pair.append((i,j))


for i in list3pair:
    print(i,end=" ")
            
