from tkinter import *
from tkinter import messagebox
import tkinter
import pickle
dict1={0:"ask"}#used to put initial value after that is of no use
#our main Contact class.

window=tkinter.Tk()
window.title("Gui")
window.geometry('400x400+100+200')

input_textid = IntVar()
input_textname = StringVar()
input_textemail = StringVar()
input_textphone = StringVar()
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
    def getPhone(self):
        return self.phonenumber
    def __str__(self):
        return "Name : "+self.name+" ,Email : "+self.emailaddress+" ,Phone-Number : "+self.phonenumber
#here file is being loaded
with open('dict1', 'rb') as a:
    dict1 =pickle.load(a)



#this fun changes name for the given id
def changeName():
    input_textname.set("")
    input_textemail.set(dict1[input_textid.get()].getEmail())
    input_textphone.set(dict1[input_textid.get()].getPhone())
    dict1[input_textid.get()].setName(input_textname.get())
    tkinter.messagebox.showinfo('Name has been updated')
#this fun changes email for the given id
def changeEmail():
    input_textname.set(dict1[input_textid.get()].getName())
    input_textemail.set("")
    input_textphone.set(dict1[input_textid.get()].getPhone())
    dict1[input_textid.get()].setEmail(input_textemail.get())
    tkinter.messagebox.showinfo('Email has been updated')
#this fun changes phonenumber for the given id
def changePhone():
    input_textname.set(dict1[input_textid.get()].getName())
    input_textemail.set(dict1[input_textid.get()].getEmail())
    input_textphone.set("")
    dict1[input_textid.get()].setEmail(input_textphone.get())
    tkinter.messagebox.showinfo('Phone has been updated')
def show():
    input_textname.set(dict1[input_textid.get()].getName())
    input_textemail.set(dict1[input_textid.get()].getEmail())
    input_textphone.set(dict1[input_textid.get()].getPhone())


#it adds new person to the dataset
def addPerson():
    for i in dict1:
        if(i==input_textid.get()):
            show()
            return
    input_textname.set("Enter name here")
    input_textemail.set("Enter mail here")
    input_textphone.set("Enter Phone Here")

#prints the obj value
def askContact():
    obj=Contact(input_textname.get(), input_textphone.get(), input_textemail.get())
    dict1[input_textid.get()] = obj
    with open('dict1', 'wb') as a:
        pickle.dump(dict1,a)
        a.close()
    tkinter.messagebox.showinfo('Info Saved Successfully')


#deletes the contact
def deleteContact():
    del dict1[input_textid.get()]
    btn_clear()
    tkinter.messagebox.showinfo('Person details deleted Successfully')


def btn_clear():
    input_textid.set(0)
    input_textname.set("")
    input_textemail.set("")
    input_textphone.set("")

#calling main

try:
    tkinter.Label(window,text="Enter Id").grid(row=0)
    ask=tkinter.Entry(window,textvariable = input_textid).grid(row=0,column=1)
    tkinter.Label(window,text="Name : ").grid(row=1)
    tkinter.Entry(window,textvariable = input_textname).grid(row=1,column=1)
    btn2=tkinter.Button(window,text="Change Name",command=changeName).grid(row=1,column=2)
    tkinter.Label(window,text="E-mail : ").grid(row=2)
    tkinter.Entry(window,textvariable = input_textemail).grid(row=2,column=1)
    btn1=tkinter.Button(window,text="Change mail",command=changeEmail).grid(row=2,column=2)
    tkinter.Label(window,text="Phone Number : ").grid(row=3)
    tkinter.Entry(window,textvariable = input_textphone).grid(row=3,column=1)
    btn4=tkinter.Button(window,text="Change Phone",command=changePhone).grid(row=3,column=2)
    btn1=tkinter.Button(window,text="Check_ID",command=addPerson).grid(row=4,column=0)
    btn2=tkinter.Button(window,text="Clear",command=btn_clear).grid(row=4,column=2)
    btn1=tkinter.Button(window,text="save",command=askContact).grid(row=4,column=1)
    btn1=tkinter.Button(window,text="delete",command=deleteContact).grid(row=5,column=1)
except:
    tkinter.messagebox.showinfo("please Enter Correctly ,Ui Under Developement")
#main()

window.mainloop()
