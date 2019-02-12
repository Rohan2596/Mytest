import random 
count=[]
sum=0
# a=int(input("Enter a"))
# b=int(input("Enter b"))
# c=int(input("Enter c"))
a= random.randint(-10,10)
b=random.randint(-10,10)
c=random.randint(-10,10)
print("Three Values a,b,c",a,b,c)
sum=a + b + c
if sum==0:
	print("Sum is zero")
else:
	print("Sum is not zero")