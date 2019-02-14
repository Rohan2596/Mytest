def recur_factorial(n):
   
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input("Enter the input :"))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))
for num in range(0,num + 1):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				
				break
			else:
				print(num)