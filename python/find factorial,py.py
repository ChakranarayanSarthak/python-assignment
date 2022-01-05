#write a python program to find the factorial of number:

num=int(input("enter the number find factorial:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial is=",fact)


#output:
#enter the number find factorial:5
#factorial is= 120
