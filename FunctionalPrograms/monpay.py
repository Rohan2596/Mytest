#converting years into months
import math
n=Y*12
p1=P*r
p2=math.pow(1/(1+r),n)
p3=1-p2
P=float(input("Enter the Principal loan amount : "))
print("Enter the number of years in months :- ",n)
print("Enter the rate of interset ")
print("Payment to be paid monthly:",p1/p3)
print("Total amount  to be paid back all together",(p1/p3)*n)
print(n,r)
print(p1,p2)
R=float(input("Enter the no of compunded interset monthly : "))
r=R/(12*100)
Y=int(input("Enter the no of years to pay:"))