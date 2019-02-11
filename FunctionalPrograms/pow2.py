# power of 2
'''n=int(input("Enter the number to find the power"))

def power():
	for i in range(0,n):
		y=math.pow(i)
		print(i,"=",n)

power()'''
n=int(input("Input number for power of 2: "))
for i in range(0,n+1):
	p2 = (i**2)
	print ( i,"=",p2 )