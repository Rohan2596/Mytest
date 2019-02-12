import datetime

m=int(input("Enter the month :"))
d=int(input("Enter the date :"))
y=int(input("Enter the year :"))
today=datetime.datetime(y,m,d)
Day=today.weekday()
print(Day)
yo=y-((14-m)/12)
x=yo +(yo/4)-(yo/100)+(yo/400)
print(yo,x)
mo= m+12*((14-m)/12)-2
do=(d+x+(31*mo/12))%7
print(x,mo,do)
if Day==0:
	print("Monday")
elif Day ==1:
	print("Tuesday")
elif Day ==2:
	print("Wednesday")
elif Day ==3:
	print("Thursday")
elif Day ==4:
	print("Friday")
elif Day ==5:
	print("Saturday")
else:
	print("Sunday")