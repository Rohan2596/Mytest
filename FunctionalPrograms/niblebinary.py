import math
def dectobinary(n):
	binaryarr=[0]*n
	i=0
	while n>0:
		binaryarr[i]=n%2
		n=int(n/2)
		i+=1
	for j in range(i-1,-1,-1):
		print(binaryarr[j],end=" ")
	return binaryarr

def binarytodec(binaryarr):
	for i in range(0,len(binaryarr)):
		if binaryarr[i]==1:
			k=math.pow(2,i)
			print(k)
		elif binaryarr[i]==0:
			
			print()
n1=int(input("Enter the value: "))
binaryarr=dectobinary(n1)
binarytodec(binaryarr)
