#write python program to print all prime  number in an interval:
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
for num in range(lower,upper+1):  
   if num>1:  
       for i in range(2,num):  
           if (num%i)==0:  
               break  
       else:  
           print(num)  


#output:
#Enter lower range: 2
#Enter upper range: 20
#2
#3
#5
#7
#11
#13
#17
#19
