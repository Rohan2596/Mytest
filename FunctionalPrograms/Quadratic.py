import math
a=int(input("enter the a: "));
b=int(input("enter the b: "));
c=int(input("enter the c: "));
delta=(b*b) - (4*a*c);
d=abs(delta);
roots1=(-b + (math.sqrt(abs(delta)))) / 2*a
print(roots1);
roots2=(-b - (math.sqrt(abs(delta)))) / 2*a
print(roots2)