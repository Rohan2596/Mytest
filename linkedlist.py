#create nodes 
# create lonked list
# add nodes to linked list
#print linked lis
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None
	def insert(self,newNode):
		#head=>john->None
		if self.head is None:
			self.head=newNode
		else:
			#head=>John->Ben->None
			lastNode=self.head
			while True:
				if lastNode.next is None:
					break
				lastNode=lastNode.next
			lastNode.next=newNode
	def printlist(self):
		currentNode=self.head
		while True:
			if currentNode is None:
				break
			print(currentNode.data)
			currentNode=currentNode.next
#node==data,next

firstNode=Node("John")
linkedlist=Linkedlist()
linkedlist.insert(firstNode)
secondNode=Node("Ben")
linkedlist.insert(secondNode)
thirdNode=Node("Mathew")
linkedlist.insert(thirdNode)		
linkedlist.printlist()