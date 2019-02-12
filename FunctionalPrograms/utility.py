class Utility:
	def temperatureConversion(c,f):
	a=c*9/5 +32
	print("Celsius to fahrenheit: ",a)
	b = (f-32)*5/9
	print("fahrenheit to Celsius: ",b)
	return a,b

	def monthlypayments():
	n=Y*12
    print("Enter the number of years in months :- ",n)
    r=R/(12*100)
    print("Enter the rate of interset ")
    print(n,r)
    p1=P*r
    p2=math.pow(1/(1+r),n)
    p3=1-p2
    print(p1,p2)
    Pay=p1/p3
    print("Payment to be paid monthly:",p1/p3)
    print("Total amount  to be paid back all together",(p1/p3)*n)
    return Pay