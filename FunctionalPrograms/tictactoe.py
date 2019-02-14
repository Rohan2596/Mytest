lst=[' ',' ',' ',' ',' ',' ',' ',' ']
print(lst)
# i=int(input("enter i"))
# j=int(input("enter j"))
# print(lst[i][j]="x")
player=int(input("Enter the Player 1 or 2 :"))
if player==1:
	print("player one")
elif player ==0:
	print("player two")
else:
	print("Player not")
i=0
while player==1:
	while i<8:
		pos=int(input("enter i"))
		if lst[pos]==' ':
			i+=1
		lst[pos]="X"
		print(lst)
	break

# while i<8:
# 	pos=int(input("enter i"))
	
# 	if lst[pos]==' ':
# 		i+=1
# 	lst[pos]="X"
# 	print(lst)

	
# if ((lst[0][0]=="X" and lst[0][1]=="X" and lst[0][2]=="X") 
# 	or (lst[1][0]=="X" and lst[1][1]=="X" and lst[1][2]=="X")
# 	or (lst[0][0]=="X" and lst[0][1]=="X" and lst[0][2]=="X")):print("Player won")