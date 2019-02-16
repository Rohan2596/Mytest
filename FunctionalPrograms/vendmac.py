notes=int(input("Enter the value"))
print("Amount Entered to into Vending machine: ",notes)
no=[]
n1=[1000,500,100,50,10,5,2,1]
i=-1
while notes>=0:
	if i<len(n1)-1:
		i+=1
	if notes>=n1[i] :	
		notes=notes-n1[i]
		print(n1[i])
		i=-1


