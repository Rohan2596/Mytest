# class daynames:
# 	def __init__(self,dataval=None):
# 		self.dataval=dataval
# 		self.nextval=None
# e1=daynames("mon")
# e2=daynames("tue")
# e3=daynames("Wed")
# e1.nextval=e3
# e3.nexval=e2
# e2.nextval=e1
# thisvalue=e2
# while thisvalue:
# 	print(thisvalue.dataval)
# 	thisvalue= thisvalue.nextval
class Node:
	def __init__(self.dataval=None):
		self.dataval=dataval
		self.nextval= None
class SlinkedList:
	def __init__(self):
		self.headval=None
list1=SlinkedList()
list1.headval=Node("MOn")
e2=Node("Tue")
e3=Node(Wed)
list1.headval.nextval=e2
e2.nextval=e3	