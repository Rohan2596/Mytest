import datetime

m=int(input("Enter the month :"))
d=int(input("Enter the day :"))
y=int(input("Enter the year :"))
today=datetime.datetime(y,m,d)
print(today.weekday())
yo=y-((14-m)/12)
x=yo +yo/4-yo/100+yo/400
print(yo,x)
mo=m+128*((14-m)/12)-2
do=(d+x+(31*mo/12))%7
print(x,mo,do)