total=int(input("Enter no of fruits"))
fruit={}#declaring fruits as dictionary
#running loop to take info
for i in range(total):
    fruit[i+1]={}
    fruit[i+1]['name']=input("Enter the name of the fruit")
    fruit[i+1]['bionomical name']=input("Enter the bionomical name for fruit")
    count=int(input("enter how many major producers are available"))
    fruit[i+1]['major_producers']={}
    for j in range(count):
        x=input()
        fruit[i+1]['major_producers'][x]={}
        fruit[i+1]['major_producers'][x]['nutrition']={}
        fruit[i+1]['major_producers'][x]['nutrition']['carbohydrates']=float(input("enter carbohydrate"))
        fruit[i+1]['major_producers'][x]['nutrition']['fat']=float(input("enter fat"))
        fruit[i+1]['major_producers'][x]['nutrition']['protein']=float(input("enter protein value"))
        #printing dictionary
print("Dictionary of Current Info",fruit)

#to find largest producer of nutrition among all in list2
#to find nutrition production in china
list2=[]
list1=[]
for fruit_id in fruit.keys():
    for nutrition in fruit[fruit_id]['major_producers'].keys():
        if(nut=="china"):
            list2.append(fruit[fruit_id]['major_producers'][nutrition]['nutrition']['protein'])
        list1.append(fruit[fruit_id]['major_producers'][nutrition]['nutrition']['protein'])
#printing Required Values
print("maximum  producer in protein is",max(list1))
#printing china value of protein
print("maximum production among major producer in protein in china is",max(list2))
