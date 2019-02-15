import numpy as np
def dectobinary(n):
	binaryarr=[0]*8
	i=0
	while n>0:
		binaryarr[i]=n%2
		n=int(n/2)
		i+=1
	for j in range(7,-1,-1):
		print(binaryarr[j],end=" ")
	return binaryarr

def swap(dec):
	j=7
	for i in range(3,-1,-1):
		temp = dec[i]
		dec[i]=dec[j]
		dec[j]=temp
		j-=1
	print()
	for j in range(7,-1,-1):
		print(dec[j],end=" ")
	

n1=int(input("Enter the decimal to calculate Binary: "))
dec=dectobinary(n1)
swap(dec)


