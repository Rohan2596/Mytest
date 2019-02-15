import numpy as np
str1=input("Enter the str1: ")
str2=input("Enter the str2: ")

#arr=np.zeros((len(str2)))
# cnt=0
# if len(str1)==len(str2):
# 	 for x in range(len(str1)):
# 	 	for y in range(len(str2)):
# 	 		if str1[x]==str2[y] and arr[y]==0:
# 	 			arr[y]=1
# 	 			cnt+=1
# 	 if cnt==len(str2):
# 	 	print("String is anagram.")
# 	 else:
# 	 	print("String is not anagram.")
# else:
# 	print("String is not Anagram")
# # from collections import Counter
# def anagram(str1,str2):
# 	if Counter(str1)==Counter(str2):
# 		print("string are anagram")
# 	else :
# 		print("not a anagram")

# anagram(str1,str2)
# Output:
# Enter the str1: 123
# Enter the str2: 123
# string are anagram

# Enter the str1: earth
# Enter the str2: heart
# string are anagram

# Enter the str1: keeo
# Enter the str2: okpp
# not a anagram

s1=list(str1)
s2=list(str2)

if len(str1)==len(str2):
	if s1.sort()==s2.sort():
		print("Anagram")

	# print("String are Anagram")
	# else:
	# 	print("String are *****(not)***** Anagram")
else:
	print("String are ****(not)*** Anagram")