def binary_sort(sorted_list, key,length,*args):
    start = 0
    end = length-1
    print(length)
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted_list[mid]:
            print("\nEntered number %s is present at position: %s" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1
#binary_sort(alist,10,6,2) 
L = ["Brian", "Joe", "Rohan","Lois", "Meg", "Peter", "Stewie"] # Needs to be sorted.

print (binary_sort(L, "Peter",6))
def insertionsort(alist):
    for i in range(1,len(alist)):
        current =alist[i]
        while i>0 and alist[i-1]>current:
            alist[i]=alist[i-1]
            i=i-1
            alist[i]=current
        #print(alist)
    return alist
print(insertionsort(L))

def buublesort(alist):
    for i in range(1,len(alist)):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp
    return alist
print(buublesort(L))