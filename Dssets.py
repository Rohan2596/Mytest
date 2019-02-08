#Dssets

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
for d in Days:
	print(d)
Days.add("no")
print(Days)
Days.discard("Sun")
print(Days)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)
AllDays= DaysA&DaysB
print(AllDays)
AllDays = Days - DaysB
print(AllDays)
subset= DaysA <= DaysB
superset = DaysA >= DaysB
print(subset)
print(superset)