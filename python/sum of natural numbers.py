#write a python program to find sum of natural numbers:

n=int(input("enter the starting number:"))
n1=int(input("enter the ending number:"))
s=0
for i in range(n,n1+1):
    s=s+i
print("sum of natural number:",s)


#output:
#enter the starting number:12
#enter the ending number:120
#sum of natural number: 7194
