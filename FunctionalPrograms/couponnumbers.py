#couponnumbers
import random
arr=[]
i=0
n1=int(input("Enter the range "))
n2=int(input(" Enter the numbers"))
for i in range(0,n1):
    n=random.randint(1,n2)
    if n not in arr:
    	arr.append(n)
    	#print(set(arr))
    	i+=1
    	print(arr)
print(arr)
# print(set(arr))