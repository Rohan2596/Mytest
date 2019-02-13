def bubblesort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]> alist[j+1]:
                temp =alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp
    return alist
    
alist=bubblesort(['f','e','d','c','b','a']) 
def binary_sort(sorted_list, key,length,*args):
    start = 0
    end = length-1
    print(length)
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted_list[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1
binary_sort(alist,'c',6,2) 
