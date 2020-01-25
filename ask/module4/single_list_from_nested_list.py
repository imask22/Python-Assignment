list1=[[1,2,3],[4,5,6],[7,8]]
list2=[x[i] for x in list1 for i in range(0,len(x))]#first one is sub ;loop
print(list2)
