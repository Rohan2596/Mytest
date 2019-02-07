def printme(str):
	print(str)
	return
printme("I  am fist call to user to be defined")
printme("Again calling to the smae function")	
def changeme(mylist):
	mylist.append([1,2,3,4])
	print("values inside the function", mylist)
	return
mylist=[10,20,30];
changeme(mylist);
print("Values outside the function:",mylist)	
def printinfo(name,age=35):
	print("name",name)
	print("age",age)
	return
printinfo(age=50,name='mike')
#printinfo(age=25)
printinfo(name='hello')

def printinfo1(arg1,*vartuple):
	print("output is ")
	print(arg1)
	for var in vartuple:
		print (var)
	return
printinfo1(10)
printinfo1(20,30,50)
total = 0
def sum(A,B):
	total=A + B
	print("Inside the function: ",total)
	return total
total=sum(10,20)
print("outside the function:",total)
