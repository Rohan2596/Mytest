with open('shoppinglist.txt','w') as fileobj:
	fileobj.write('tomato\npasta\ngarlic')
with open('shoppinglist.txt','r') as fileobj:
	lines=fileobj.readlines()
print(lines)

with open('shoppinglist.txt','r') as fileobj:
	content =fileobj.read()
	lines=[]
	for line in fileobj:
		lines.append(line.strip())

fileobj=open('shoppinglist.txt','r')
pos=fileobj.tell()
print("we are at %u."%pos)
content=fileobj.read()
end=fileobj.tell()
print("this file was %u character long."%end)
fileobj.close()