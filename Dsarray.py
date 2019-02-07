from array import *
#defining the array
array1= array('i',[10,20,30,40,50])
print("All the Array elements")
for x in array1:
	print(x)

print("Accessing Array Elements")
print(array1[0])
print(array1[2])
print("Inserting the elements")
array1.insert(1,60)
for x1 in array1:
	print(x1)
print("Deletion of elements ")
array1.remove(40)
for x2 in array1:
	print(x2)
print("Search Options")
print(array1.index(50))
print("Updating the option")
array1[2]=80
for x3 in array1:
	print(x3)
'''All the Array elements
10
20
30
40
50
Accessing Array Elements
10
30
Inserting the elements
10
60
20
30
40
50
Deletion of elements 
10
60
20
30
50
Search Options
4
Updating the option
10
60
80
30
50'''	