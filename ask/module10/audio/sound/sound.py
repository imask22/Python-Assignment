import winsound

number=(input("Enter your number b: "))
one_place={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
two_place={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
           19:"ninteen",1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fivty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
digit={1:one_place,2:two_place,3:" hundred ",4:" thousand "}
str2=list(number)
length=len(str2)
str1=""
for i in str2:
    if(len(number)==1 and i=='0'):
        str1+=one_place[int(i)]
    if(i=='0'):
        length-=1
        continue
    if(length==2 and (int(number[-2:]) in range(11,20))):
        str1+=two_place[int(number[-2:])]
        break
    elif(length>=3):
        str1+=one_place[int(i)]+digit[length]
    else:
        overall=digit[length]
        str1+=overall[int(i)]+" "
    length-=1
print(str1)
list1=[]
list1=str1.split(" ")
for a in list1:
    k=a+".wav"
    winsound.PlaySound(k, winsound.SND_FILENAME)
#all sounds are working

