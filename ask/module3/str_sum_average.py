str1=input()
list1=list(str1.split(" "))
list2=[]
for i in list1 :
    if i[0].isalpha() or i[0]=="=":
        list1.remove(i)
        
list1=[int(x) for x in list1]
print("sum = ",sum(list1))
print("average = ",(sum(list1)/(len(list1)*100))*100)


