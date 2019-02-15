#newtonsqrt.py
import math
c=int(input("Enter the non negative numbers:- "))
t=c
t=(c/t + t)/2
eps=1*(math.e)-15
while  math.fabs(t-c/t)>eps*t:
	print("greater")
	break





