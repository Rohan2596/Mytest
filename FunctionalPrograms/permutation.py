from itertools import permutations
n=input("Enter the string to permutation")
n1=list(n)
perm=permutations(n1,len(n1))
print(perm)
for i in list(perm):
	print(i)
