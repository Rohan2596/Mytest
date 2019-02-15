import numpy as np
m=int(input("Enter the number of rows:"))
n=int(input("Enter the number of columns: "))

Matrix = [[0 for x in range(m)] for y in range(n)] 
Matrix1=np.zeros((m,n))
print(Matrix)
print(Matrix1)
# Matrix3=[[]]
# Matrix3=[0 for x in range(m) for y in range(n)] 

for x in range(m):
	for y in range(n):
		print("0",end=" ")
	print()
