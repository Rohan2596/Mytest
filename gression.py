import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
########################
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

serachobj=re.search(r'(.*) are (.*?).*',line,re.M|re.I)
if serachobj:
	print("Searchobj.group():",serachobj.group())
	print("Searching.group(1):",serachobj.group(1))
	print("Searching.group(2):",serachobj.group(2))
else:
	print( "Nothing found!!")
#############################################
if matchObj:
	print("match---> matchObj.group():",matchObj.group())
else:
	print ("no match!!")
######################################
if serachobj:
	print("serach---> searchobj.group():",serachobj.group())
else:
	print("nothing found!!")
#######################################################
phone="2004-568-869# this iss phone number"
num= re.sub(r'#.*$',"",phone)
print("phone  num: ",num)
num=re.sub(r'\D',"",phone)
print("phone Num:",num)