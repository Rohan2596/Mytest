num=int(input("Enter the Range to find"))
a=[]
for num in range(0,num+1):
	if num>1:
		for i in range(2,num):
			if (num%i)==0:break
		else:
			a.append(num)

a1=list(a)
print(a1)
# newarr=[]
# for i in range(len(a1)-1):
# 	for j in range(1+i,len(a1)):
# 		if len(a1[i])==len(a1[j]):
# 			for x in a1[i]:
# 				for y in a1[j]:
# 					if set(x)&set(y)==set():
# 						newarr.append(a1[i])
# 						newarr.append(a1[j])
# 						#break
# 					else:
# 						print("String are not anagram")
# 		else: print("String is not Anagram")

# print(newarr)

newarr=[]
i=0
for i in range(len(a1)-1):
	for j in range(i+1,len(al)):
		arr=np.zeros((len(str2)))
		cnt=0
		str1 = str(a1[i])
		str2 = str(a1[j])
		if len(str1)==len(str2):
	 		for x in range(len(str1)):
	 			for y in range(len(str2)):
	 				if str1[x]==str2[y] and arr[y]==0:
	 					arr[y]=1
	 					cnt+=1
	 		if cnt==len(str2):
	 			print("String is anagram.")	
	 		else:
	 			print("String is not anagram.")
        else:
        	print("String is not Anagram")
print(newarr)
