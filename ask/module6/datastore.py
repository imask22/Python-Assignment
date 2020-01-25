#......................ATTENTION................program wont work if you dont have tabulate.....@ask.
#to install it use--------->
#set TABULATE_INSTALL=lib-only
#pip install tabulate__for windows
#pip install tabulate for ubuntu/linux
try:
    from tabulate import tabulate
except:
    print("please install tabulate")
#datastore={"office":{"medical1":[{"room-number":100,"use":"reception","sq-ft":50,"price":75},{"room-number":101,"use":"waiting","sq-ft":250,"price":75},{"room-number":102,"use":"examination","sq-ft":125,"price":150},{"room-number":103,"use":"examination","sq-ft":125,"price":150},{"room-number":104,"use":"office","sq-ft":150,"price":100}],"parking1":{"location":"premium","style":"covered","price":750}}}

datastore={}

try:
    filein=open('ask.txt','r')
    ask=filein.read()
    datastore=eval(ask)
except:
    print("make sure txt file must be in same folder as program")
    
#this method is to change the use value of medical field of a particular office...
def setuse():
    try:
        field=input("Enter field : ")
        subfield=input("Enter subfield : ")
        if(datastore[field][subfield]):
            pass
        print("Enter room : ")
        room=int(input())
        print("Enter use value : ")
        use=input()
        for i in range(len(datastore[field][subfield])):
            if(datastore[field][subfield][i]['room-number']==room):
                datastore[field][subfield][i]["use"]=use
                break
    except KeyError:
        print("Please enter correct Field or SubField")
    except:
        print("Room no value must be an Integer")
    else:
        print("Successfully changed use value")
    
#this method is to change the price value of medical field of a particular office...
def setprice():
    try:
        field=input("Enter field : ")
        subfield=input("Enter subfield : ")
        if(datastore[field][subfield]):
            pass
        room=int(input("Enter room : "))
        price=input("Enter use price : ")
        for i in range(len(datastore[field][subfield])):
            if(datastore[field][subfield][i]['room-number']==room):
                datastore[field][subfield][i]["price"]=price
                break
    except KeyError:
        print("Please enter correct Field or SubField")
    except:
        print("Room no value must be an Integer")
    else:
        print("Success fully changed price value")
        
#this method is to change the ROOM NUMBER value of medical field of a particular office...
def setroomno():
    try:
        field=input("Enter field : ")
        subfield=input("Enter subfield : ")
        if(datastore[field][subfield]):
            pass
        print("Enter room : ")
        room=int(input())
        print("Enter use roomno : ")
        roomno=int(input())
        for i in range(len(datastore[field][subfield])):
            if(datastore[field][subfield][i]['room-number']==room):
                datastore[field][subfield][i]["roomno"]=roomno
                break
    except KeyError:
        print("Please enter correct Field or SubField")
    except:
        print("Room no value must be an Integer")
    else:
        print("Success fully changed room number value")

#dynamically take parking or medical according to user input  --imp--            
def getinfo():
    list1=[]
    try:
        field=input("Enter field : ")
        subfield=input("Enter subfield : ")
        if(datastore[field][subfield][0]):
            pass
        medic=subfield
        print("Enter room no :")
        room=int(input())
        for i in range(len(datastore[field][medic])):
            if(datastore[field][medic][i]['room-number']==room):
                list1.append(datastore[field][medic][i]['room-number'])
                list1.append(datastore[field][medic][i]['use'])
                list1.append(datastore[field][medic][i]['sq-ft'])
                list1.append(datastore[field][medic][i]['price'])
                list2=['room-number','use','sq-ft','price']
                print(tabulate([list1],headers=list2,tablefmt="grid"))
                print("successfully print the value")
    except KeyError:
        print('Enter Correct office/parking/medical name!!!')
    
    except:
        nm=subfield
        list1.append(datastore[field][nm]['location'])
        list1.append(datastore[field][nm]['style'])
        list1.append(datastore[field][nm]['price'])
        list2=['location','style','price']
        print(tabulate([list1],headers=list2,tablefmt="grid"))
        
                
#this method add's new office to an exsisting organization
def addfield():
    offnm=input("Enter office name : ")
    medic=input("Enter medical name : ")
    park=input("Enter Parking name : ")
    datastore[offnm]={medic:{},park:{}}
    print("successfully added the field")
    
#this used to insert detail in any medic of aby office
def enter_in_medic_of_any_field():
    try:
        of=input("Enter office name : ")
        medic=input("Enter medic name : ")
        datastore[of][medic]=[]
        print("Enter the details : ")
        i=len(datastore[of][medic])
        
        dict1={}
        dict1['room-number']=int(input("Enter room number : "))
        dict1['use']=input("Enter use for the room : ")
        dict1['sq-ft']=input("Enter sq-ft for room :  ")
        dict1['price']=input("Enter room price : ")
        datastore[of][medic].append(dict1)
    except:
        print("Enter correct medical/office name")
#this creates a new medical
def create_a_medic_in_any_field():
    try:
        of=input("Enter office name : ")
        medic=input("Enter new medic name : ")
        datastore[of][medic]=[]
        print("successfully created new medic field!!!")
    except:
        print("Please Enter correct Field/Office Name")

#this creates a new parking with values    
def enter_in_parking_of_any_field():
    of=input("Enter office name : ")
    try:
        for a in datastore[of]:
            break
        park=input("Enter parking name : ")
        datastore[of][park]={}
        datastore[of][park]['location']=input("Enter location of parking : ")
        datastore[of][park]['style']=input("Enter style of parking : ")
        datastore[of][park]['price']=input("Enter price of parking : ")
        file1=open('ask.txt','w')
        file1.write(str(datastore))
        file1.close()
        print("Entered sucessfully")
    except:
        print("Error !!!enter correct office name")
        
#show all values in a particular medical field in an particular organization
def showallmedicoffield():
    try:
        field=input("Enter office name : ")
        medic=input("Medical name : ")
        list1=[]
        list2=[]
        for i in range(0,len(datastore[field][medic])):
            list1=[]
            list1.append(datastore[field][medic][i]['room-number'])
            list1.append(datastore[field][medic][i]['use'])
            list1.append(datastore[field][medic][i]['sq-ft'])
            list1.append(datastore[field][medic][i]['price'])
            list2.append(list1)
        list3=['room-number','use','sq-ft','price']
        print(tabulate(list2,headers=list3,tablefmt="grid"))
    except:
        print("Wrong Field or Subfield!!!")
        
        
        
#show all values in a particular parking field in an particular organization
def showallparkoffield():
    try:
        field=input("Enter office name : ")
        parking=input("Enter parking name : ")
        list1=[]
        list1.append(datastore[field][parking]['location'])
        list1.append(datastore[field][parking]['style'])
        list1.append(datastore[field][parking]['price'])
        list3=['location','style','price']
        print(tabulate([list1],headers=list3,tablefmt="grid"))
    except:
        print("Wrong Field or Subfield!!!")
#save the current values to a file...........!!!
def save():
    print("Now Saving...Please wait..")
    file1=open('ask.txt','w')
    file1.write(str(datastore))
    file1.close()
    
#dictionary is better choice but its taking value of first function only-----unknown error
def choose(n):
    if(n==0):
        manual()
    elif(n==1):
        setuse()
    elif(n==2):
        setprice()
    elif(n==3):
        setroomno()
    elif(n==4):
        getinfo()
    elif(n==5):
        addfield()
    elif(n==6):
        enter_in_medic_of_any_field()
    elif(n==7):
        enter_in_parking_of_any_field()
    elif(n==8):
        showallmedicoffield()
    elif(n==9):
        showallparkoffield()
    elif(n==10):
        print(datastore)
    elif(n==11):
        save()
    else:
        print("Enter correct choice !!!")
        
#it prints manual if required    
def manual():
    print("Enter 0 to print manual : ")
    print("Enter 1 for Alter use of the dictionary's particular field's subfield : ")
    print("Enter 2 for Alter price of the dictionary's particular field's subfield : ")
    print("Enter 3 for Alter Room Number of the dictionary's particular field's subfield : ")
    print("Enter 4 for to get particular info : ")
    print("Enter 5 to create a new office : ")
    print("Enter 6 to add value in medical field : ")
    print("Enter 7 to add value in parking field : ")
    print("Enter 8 for showing all value of a particular medical field : ")
    print("Enter 9 for showing all values of a particular parking field : ")
    print("Enter 10 to dump all values : ")
    print("Enter 11 to save : ")
    print("Enter 12 to exit : ")
    print("Enter 13 to save&exit : ")
manual()



#______driver code_________
n=-1
while(n!=13 or n!=12):
    try:
        n=int(input("Enter your choice : "))
        if n==12:
            print("Bye")
            break
        elif(n!=12):
            choose(n)
        elif(n==13):
            print("Saving...the update")
            file1=open('ask.txt','w')
            file1.write(str(datastore))
            file1.close()    
            break
            
    except:
        print("Some error occured : (input only integer or value between (0-12))")
        file1=open('ask.txt','w')
        file1.write(str(datastore))
        file1.close()
