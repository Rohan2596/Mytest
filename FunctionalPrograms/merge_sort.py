alist=[]
def merge_sort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
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
alist=[]
# def mergesort(alist):
#     if len(alist)>1:
#         mid=len(alist)//2
#         lefthalf=alist[:mid]
#         righthalf=alist[mid:]

#         i=0
#         j=0
#         k=0
#         while i<len(lefthalf) and j<len(righthalf):
#             if lefthalf[i]<righthalf[j]:
#                 alist[k] =lefthalf[i]
#                 i+=1
#             else:
#                 alist[k]=righthalf[j]
#                 j+=1
#             k=k+1
#         while i<len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1
#         while j< len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print("Merging",alist)
# alist=[54,26,97,8,98]
# mergesort(alist)
# print(alist)