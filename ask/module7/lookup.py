import pickle
dict1={0:"ask"}#used to put initial value after that is of no use
#our main Contact class
class Contact:
    def __init__(self,name,phonenumber,emailaddress):
        self.name=name
        self.phonenumber=phonenumber
        self.emailaddress=emailaddress
    def setEmail(self,email):
        self.emailaddress=email
    def setPhone(self,phone):
        self.phonenumber=phone
    def setName(self,name):
        self.name=name
    def getEmail(self):
        return self.emailaddress
    
    def getName(self):
        return self.name
    def getPhone():
        return self.phonenumber
    def __str__(self):
        return "Name : "+self.name+" ,Email : "+self.emailaddress+" ,Phone-Number : "+self.phonenumber
#here file is being loaded
with open('dict1', 'rb') as a:
	dict1 =pickle.load(a)

         

#this fun changes name for the given id    
def changeName():
    id1=int(input('Enter id : '))
    nm=input("Enter New Name : ")
    dict1[id1].setName(nm)
    print("Name has been updated!!!")
#this fun changes email for the given id
def changeEmail():
    id1=int(input('Enter id : '))
    nm=input("Enter New Mail : ")
    dict1[id1].setEmail(nm)
    print("Email has been updated!!!")
#this fun changes phonenumber for the given id
def changePhone():
    id1=int(input('Enter id : '))
    nm=input("Enter New Name : ")
    dict1[id1].setPhone(nm)
    print("Phone Number has been updated!!!")
    
    
#it adds new person to the dataset    
def addPerson():
    id1=int(input("Enter id : "))
    name=input("Enter your Name : ")
    email=input("Enter your Email : ")
    phone=input("Enter your Number : ")
    obj=Contact(name,phone,email)
    dict1[id1]=obj
    
    print("Person added Successfully! press 5 to save")

#prints the obj value
def print1():
    id1=int(input("Enter id : "))
    print(dict1[id1])
#write the updated values to the file
def save():
    with open('dict1', 'wb') as a:
        pickle.dump(dict1,a)
        a.close()
    print("Info Saved Successfully !!!")
    
#deletes the contact with relevent id    
def deleteContact():
    id1=int(input("Enter id to delete Contact : "))
    del dict1[id1]
    print('Person details deleted Successfully')


#__main__and Driver Code
def main():
    n=-1
    while(n!=9):
        try:
            print("Enter 0 to add new person info : ")
            print("Enter 1 to change name : ")
            print("Enter 2 to change Email : ")
            print("Enter 3 to change Phone Number : ")
            print("Enter 4 to print : ")
            print("Enter 5 to Save : ")
            print("Enter 6 to Delete a Contact : ")
            print("Enter 7 to get dict dump: ")
            print("Enter 8 to Save & Exit: ")
            print("Enter 9 to Exit: ")
            
            
            n=int(input())
            if(n==0):
                addPerson()
            elif(n==1):
                changeName()
            elif(n==2):
                changeEmail()
            elif(n==3):
                changePhone()
            elif(n==4):
                print1()
            elif(n==5):
                save()
            elif(n==6):
                deleteContact()
            elif(n==7):
                print(dict1)
            elif(n==8):
                save()
                break
            elif(n==9):
                print("Thanks For Choosing this Software!!!")
                      
            
        except:
            print("Please Enter Correct value at Correct Places")
#calling main                   
main()

