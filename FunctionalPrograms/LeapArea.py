year=int(input("Enter the Year: "))
y=str(year)
if len(y)==4:
	print("Valid year")
	if (year%4 ==0 & year%100!=0 | year %400):
		print("Year,It is leap Year")
	else:
		print("Year,It is not Leap Year")
else:
	print("Invalid Year")
'''OUTPUT:
Enter the Year: 2020
Valid year
Year,It is leap Year'''
