class person(object):
	species="home sapiens"
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return self.name
	def rename(self,renamed):
		self.name=renamed
		print("now my name is {}".format(self.name))
kelly=person("kelly")
joseph=person("joseph")
john_doe=person("john_Doe")
class A(object):
	def __init__(self,num):
		self.num=num
	def __add__(self,other):
		return A(self.num +other.num) 