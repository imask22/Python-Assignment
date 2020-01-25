people={1:{'name':'john','age':'27','sex':'male'},2:{'name':'Marie','age':'22','sex':'Female'}}
#list checking
print(people)
print(people[1])
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3]={}#declaring a new list element
#entering values in new list elements
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='no'#extra key
#declaring a new list element
people[4]={}
#entering values in new list elements

people[4]['name']='Peter'
people[4]['age']='29'
people[4]['sex']='Male'
people[4]['married']='Yes'
print(people)
#deleting the married ky of third element(key)
del people[3]['married']
del people[4]['married']
print(people)
