
import time
alist=[]
start=time.time()
def merge_sort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        print(mid)
        print(lefthalf)
        print(righthalf)
        for i in range(1,len(lefthalf)):
            for j in range(i):
                if lefthalf[j]> lefthalf[j+1]:
                    temp=lefthalf[j]
                    lefthalf[j]=lefthalf[j+1]
                    lefthalf[j+1]=temp
                    i+=1
        print(lefthalf)   
     
        for i  in range(1,len(righthalf)):
            for j in range(i):
                if righthalf[j] > righthalf[j+1]:
                    temp=righthalf[j]
                    righthalf[j]=righthalf[j+1]
                    righthalf[j+1]=temp
        print(righthalf)
        for i in range(1,len(alist)):
            for j in range(i):

                if alist[j]>alist[j+1]:
                    temp=alist[j]
                    alist[j]=alist[j+1]
                    alist[j+1]=temp
    print(alist)
merge_sort([1,13,11,100,52,89,98])
end=time.time()
t1=end-start
print(t1*10000)
