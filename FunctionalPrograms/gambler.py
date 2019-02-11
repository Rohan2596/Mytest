import random
total_money=1
count=0
goal=int(input("enter the goal Amount:"))

while total_money<goal:
	if total_money==0: 
		break
	n= int(input("Enter the Bet Number:"))
	n1=random.randint(1,2)
	print(n1)
	if (n == n1):
		print("Gambler won!!")
		total_money+=1
    	#print("total_money won", total_money)
	else:
		print("Gamlber lost!! ")
		total_money-=1

