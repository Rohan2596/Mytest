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
my_function()'''
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


