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
