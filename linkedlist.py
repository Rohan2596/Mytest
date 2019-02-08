class daynames:
	def __init__(self,dataval=None):
		self.dataval=dataval
		self.nextval=None

e1=daynames('mon')
e2=daynames('Tue')
e3=daynames('Wed')
e1.nextval=e3
e3.nextval=e2
thisvalue=e1
while thisvalue:
	print(thisvalue.dataval)
	thisvalue=thisvalue.nextval