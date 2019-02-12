 n1=float(input("Enter the value Celsius: "))
 n2=float(input("enter the value for fahrenheit: "))
def temperatureConversion(c,f):
 	a=c*9/5 +32
 	print("Celsius to fahrenheit: ",a)
 	b = (f-32)*5/9
 	print("fahrenheit to Celsius: ",b)
 	return a,b
 temperatureConversion(n1,n2)