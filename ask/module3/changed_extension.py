str1=str(input("Enter full file path :"))
print((str1.split("/")[-1].split(".")[0]),end=".pdf")
