#Windcchill
import math
w=[]
w1=[]
w2=[]
w3=[]
t=float(input("Enter the temperature in Fahrenheit:-  "))
v=float(input("enter the Windspeed in miles pe hour:-  "))
w1 =35.74 +0.6215*t
w2 =0.4275*t - 35.75
w3 =math.pow(v,0.16)
print(w1,"  ",w2,"  ",w3)
w= w1 + (w2*w3)
# print(w)
if ((t <=50) and (3<=v>=120)):
	print("Valid Year")
	print(w)

else:
	print("InValid Year")

