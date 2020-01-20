n=int(input("Enter number of Packages purchased : "))
amount=n*99

if(n>=100):
    discount=40
elif(n>=50):
    discount=30
elif(n>=20):
    discount=20
elif(n>=10):
    discount=10
else:
    discount=0


if discount:#(if any is mentioned in the question)
    print("Discount = $",(amount*discount)/100)
print("Total Amount $",amount-(amount*discount)/100)
