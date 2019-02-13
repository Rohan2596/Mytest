fo=open("foo.txt","r")
str=fo.read()
print("read:   ",str)
def convert(string):
	li=list(string.split(" "))
	return li
print(convert(str))
str1=convert(str)
def bubble_sort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j]> alist[j+1]:
				temp=alist[j]
				alist[j]=alist[j+1]
				alist[j+1]=temp
	return alist
print(len(str1))
print(bubble_sort(str1))
def binary_sort(sorted_list,key,*args):
	start=0
	end=len(sorted_list)-1
	print(len(sorted_list))
	while start<=end:
		mid = int((start + end)/2)
		if key ==sorted_list[mid]:
			print("\nEntered number %s is present at position:%s",(key,mid))
			return -1
		elif key < sorted_list[mid]:
			end =mid -1
		elif key >sorted_list[mid]:
			start=mid +1
	print("\n Element not found!")
	return -1
print(binary_sort(str1,"Python"))


fo.close()