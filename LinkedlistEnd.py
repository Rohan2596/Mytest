class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None
	def insertHead(self,newnode):
		#data=>Mathew,next=>None
		temporaryNode=self.head#john
		self.head=newnode
		self.head.next=temporaryNode
		del temporaryNode

	def insertEnd(self,newNode):
		if self.head is None:
			self.head=newNode
		else:
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


firstNode=Node("John")
linkedlist=Linkedlist()
linkedlist.insertEnd(firstNode)
secondNode=Node("Ben")
linkedlist=Linkedlist()
linkedlist.insertEnd(secondNode)
thirdNode=Node("Mthews")
linkedlist.insertHead(thirdNode)
linkedlist.printlist()