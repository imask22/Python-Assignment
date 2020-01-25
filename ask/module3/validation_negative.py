print("enter exit to exit the loop")
while(1):
    ask=input("Enter no of product = ")
    whp=input("Enter wholesale price : ")
    if(whp=="exit"):
        break
    elif("-" in whp):
        continue
    else:
        whp=float(whp)
        print("retail price = ",whp*0.5*float(ask))    
