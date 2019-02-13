# def bubblesort(alist):
#     for i in range(len(alist)-1,0,-1):
#         for j in range(i):
#             if alist[j]> alist[j+1]:
#                 temp =alist[j]
#                 alist[j]=alist[j+1]
#                 alist[j+1]=temp
#     return alist
# # print(bubblesort([5,5,1,4,2,10]))
# def insertionsort(alist):
#     for i in range(1,len(alist)):
#         current =alist[i]
#         while i>0 and alist[i-1]>current:
#             alist[i]=alist[i-1]
#             i=i-1
#             alist[i]=current
#         print(alist)
#     return alist
# print(insertionsort([5,2,3,6,1,8]))

