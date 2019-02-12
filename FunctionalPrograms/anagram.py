str1=input("Enter the str1:    ")
str2=input("Enter the str2: ")
s1=list(str1)
s2=list(str2)
print("String List s1",s1)
print("String list S2",s2)
if len(s1)==len(s2) :
	if s1==s2:
		print("String are anagram")
	else:
		print("String are not anagram ")
else:
	print("String is not Anagram")
# from collections import Counter
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
