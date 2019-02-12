def buublesort(alist):
	for i in range(1,len(alist)):
		for j in range(i):
			if alist[j]>alist[j+1]:
				temp=alist[j]
				alist[j]=alist[j+1]
				alist[j+1]=temp
	return alist
print(buublesort([5,5,1,0,8,7]))