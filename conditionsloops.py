n1=float(input("Enter the First number: "))
if n1 >=0:
	print("the number is positive")
else:
	print("number is negative")

n2=float(input("Enter the second number: "))
if n2 % 2==0:
	print("Its is Even number")
elif n2 % 2 !=0:
	print("Its is odd number")
else:
	print("Conditions is invalid")
n3=int(input("enter the year: "))
if len(str(n3))==4:
	print("Valid input")
	if n3 % 4 ==0:
		print("Year is leap ")
	else :
		print("Year is not leap year")
else:
	print("conditions is invalid")
n4=int(input("Enter a number:"))
if n4>1:
	for i in range(2,n4):
		if (n4 % i)==0:
			print(n4,"is not a prime number")
			print(i,"times",n4//i ,"is",n4)
			break
		else:
			print(n4,"is not a prime number")
else:
	print(n4,"Is not a prime number ")
na=int(input("Enter lower range: "))
up=int(input("enter upper range:"))
for num in range(na,up+1):
    if num>1:
    	for j in range(2,num):
    		if (num%j)==0:
    			
    			break
    		else:
    			print(num)
num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial) 
num1 = int(input("Show the multiplication table of?"))  
    # using for loop to iterate multiplication 10 times  
for i in range(1,11): print(num1,'x',i,'=',num1*i)

nterms=int(input("How many terms you want? "))
n6=0
n7=1
count=2
if nterms<=0:
	print("Please enter the positive numbers")
elif nterms ==1:
	print("fibonacci sequence:")
	print(n1,",",n2,end=",")
while count<nterms:
		nth=n6 +n7
		print(nth,end=',')
		n6=n7
		n7=nth
		count +=1