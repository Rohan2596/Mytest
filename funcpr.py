'''def func(*args):
	for i in args:
		print(i)
func(1,2,3)'''
def func(**kwargs):
	for name,value in kwargs.items():
		print(name,value)
func(value1=1,value2=2,value3=3)
func()
my_dict={'foo':1,'bar':2}
func(**my_dict)
def append(elem,to=[]):
	to.append(elem)
	return to
print(append(1))
print(append(2))
print(append(3,[]))
def fibonacci(n):
	def step(a,b):
		return b,a+b
	a,b =0,1
	for i in range(n):
		a,b=step(a,b)
	return a
print("fibonacci Series:-",fibonacci(5))
def cursing(depth):
	try:
		cursing(depth +1)
	except RuntimeError as RE:
		print('I recursed {} times!.',format(depth))
cursing(0)
import sys
print(sys.getrecursionlimit())
lambda_factorial=lambda q:1 if q==0 else q*lambda_factorial(q-1)
print(lambda_factorial(4))