'''# userinput and repace string
username=str(input("Enter the Username for the Input: "))
print("Hello",username,"How are you")
#leap Year
year=int(input("Enter the Year find leap or not: "))
y=str(year)
if len(y) == 4:
	print("Valid year")
	y1=int(y)
	if (y1%4==0 and y1%100!=0 or y1%400==0):
		print("Year is leap")
	else:
		print("Year is not Leap")
else:
	print("Invalid Year")
n=int(input("Input number for power of 2: "))
for i in range(0,n):
	p2=i**2
	print(i,"=",p2)
n=int(input("Input number for harmonic number:"))
if n!=0:
	for i in range(1,n+1):
		h2=(1/i)
		print(i,"=",h2)
		#print(sum(map(double,h2)))
else:print("Invalid String")'''
'''def super_secret_function(f):
	return f
@super_secret_function
def my_function():
	print("This functions no lontger be called...")
my_function()
def print_args(func):
	def inner_func(*args,**kwargs):
		print(args)
		print(kwargs)
	return func(*args,**kwargs):
return inner_func
@print_args
def multiply(num_a,num_b):
	return num_a*num_b
print(multiply(3,5))
import math
x=int(input("enter the x value: "))
y=int(input("enter the y value: "))
def euclidean(x,y):
	z=((x*x) + (y*y))
	euclidean_dis=math.sqrt(z)
	return euclidean
print(euclidean)'''
####Qudractic equation
'''import math
a=int(input("enter the input to for roots:"))
b=int(input("enter the input to for roots:"))
c=int(input("enter the input to for roots:"))
print(a,b,c)
delta=((b*b) - (4*a*c))
x=math.sqrt(delta)
x1=((-b + x ))/(2*a)
#x2= ((-b - (math.sqrt(delta)))/(2*a)
'''
# a=int(input("Enter a"))
# b=int(input("Enter b"))
# c=int(input("Enter c"))
# sum= a+b+c
# if sum ==0:
# 	print("Sum is zero")
# # else:
# # 	print("SUm is not")
# def temperatureConversion(f,c):
# 	a=c*9/5 +32
# 	print("Celsius to fahrenheit: ",a)
# 	b = (f-32)*5/9
# 	print("fahrenheit to Celsius: ",b)
# 	return a,b
# temperatureConversion(45,12)

# n1=int(input("enter the lower limit"))
# n2=int(input("rnter the upper limit"))
# for num in range(1,1000):
# 	if num>1:
# 		for i in range(num):
# 			if (i%num)==0:
# 				breakprint(i)
# def is_prime():
# 	for i in range(101):
# 		for j in range(2,i-1):
# 			if i%j==0: break
#             else:
#             print (i)	
# is_prime()
import math
c=int(input("enter the nonnegative number:"))
t=c
p1=math.fabs(t-c/t)
print(p1)

