n=int(input())
reversed_num=0
while(n>0):
    reversed_num=reversed_num+int(n%10)
    n=int(n/10)
    reversed_num*=10
print(int(reversed_num/10))

