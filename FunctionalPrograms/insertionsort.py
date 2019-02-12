def insertionsort(alist):
	for i in range(1,len(alist)):
		current =alist[i]
		while i>0 and alist[i-1]>current:
			alist[i]=alist[i-1]
			i=i-1
			alist[i]=current
	    #print(alist)
	return alist
print(insertionsort([5,2,3,6,1,8]))