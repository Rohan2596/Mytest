import random
n=int(input("enter the number :"))
n1=random.random()
i=0
if n==n1:
	print("Gambler won the bet")
	i=i+1
	for j in range(i):
		print(sum(i))
else:
	print("Gambler lost the bet")
	i=i-1
	for k in range(i):
		print(sum(i))