# Harmonic Series
import math
n=int(input("Enter the number to find the harmonic value of :"))
if n==0:
	print("the harmonic value is zero")
elif n!=0:
	for i in range(1,n):
		h2=1/i;
		print(i,"=","{:10.4f}".format(h2))
		i+=1
		
else:
	print("Invalid series")
  
