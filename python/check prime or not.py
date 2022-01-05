#python program to check prime number:

num=int(input("enter the number to check:"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
if(flag==0):
    print("the number you enter is prime:")
else:
    print("the number you enter is not prime:")
        

#output:
#enter the number to check:7
#the number you enter is prime:


#enter the number to check:22
#the number you enter is not prime:
