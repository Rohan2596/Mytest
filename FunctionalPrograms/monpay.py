import math
P=float(input("Enter the Principal loan amount : "))
Y=int(input("Enter the no of years to pay:"))
R=float(input("Enter the no of compunded interset monthly : "))
#converting years into months
n=Y*12
print("Enter the number of years in months :- ",n)
r=R/(12*100)
print("Enter the rate of interset ")
print(n,r)
p1=P*r
p2=math.pow(1/(1+r),n)
p3=1-p2
print(p1,p2)
print("Payment to be paid monthly:",p1/p3)
print("Total amount  to be paid back all together",(p1/p3)*n)