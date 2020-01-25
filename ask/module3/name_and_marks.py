str1=input()
listask=list(str1.split(","))

list1=list(str1.split(","))[1:]
list1=[int(x) for x in list1]
agg=""
print(listask[0]," got ",sum(list1[:5]),"marks out of 500 marks in theory and", sum(list1[5:]),"marks out of 30 and successfilly passed the exam with "+"{:.2f}".format(((sum(list1[:])/590)*100)),"in aggeregate, many congratulations to the ",listask[0])
