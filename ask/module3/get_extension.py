str1=str(input("Enter full file name : "))
str2=""
list1=[str(x) for x in str1]
ask=list1.index(".")
print(str2.join(list1[ask+1:]))

