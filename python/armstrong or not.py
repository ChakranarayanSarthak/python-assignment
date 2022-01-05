#write a python program to find number is armstrong or not:

num=int(input("Enter the number to check:"))
s=0
temp=num
while(temp>0):
    d=temp%10
    s+=d*d*d
    temp//=10
if(num==s):
    print("the number you enter is armstrong:")
else:
    print("the number you enter is not armstrong:")


#output:
#1:Enter the number to check:370
#the number you enter is armstrong:
#2:Enter the number to check:123
#the number you enter is not armstrong:
