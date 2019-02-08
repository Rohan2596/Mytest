import random
import calendar
yy=int(input("Enter the year: "))
mm=int(input("Enter month: "))
print(random.randint(100,500))
print("hello world")
x= int(input("enter the number 1:",))
y=int(input("enter the number 2:"))
sum=x+y
area=0.5*x*y
temp=x
x=y
y=temp
print(x,y)
print(sum)
print(area)
print(calendar.month(yy,mm))