'''from enum import Enum
class color(Enum):
	red=1
	green=2
	blue=3
print(color.red)
print(color(1))
print(color['red'])
print([c for c in color])
def counter():
	num=0
	def incremanter():
		nonlocal num
		num+=1
		return num
	return incremanter
c=counter()
c()
c()
c()
a="global"
class Fred:
	x='class'
	b=(a for i in range(10))
	c=[a for i in range(10)]
	d=a
	e=lambda :a
	f=lambda a=a:a
	def g():
		return a
print(Fred.a)
print(next(Fred.b))
print(Fred.c[0])
print(Fred.d)
print(Fred.e())
print(Fred.f())
print(Fred.g())

for index,item in enumerate(['one','two','three','four']):
	print(index,'::',item)
x=map(lambda e: e.upper(),['one','two','three','four'])
print(list(x)) 
###
import itertools 
options={"x": ["a", "b"],
         "y": [10, 20, 30]}
keys=options.keys()
values=(options[key] for key in keys)
combinations=[dict(zip(keys,combination)) for combination in itertools.product(*values)]
print(combinations)
from operator import itemgetter,attrgetter
people=[{'name':'chandan','age':20,'salary':2000},
{'name':'chetan','age':18,'salary':5000},
{'name':'guru','age':30,'salary':3000}]
by_age=itemgetter('age')
#by_salary=itemgetter('salary')
print(people.sort(key=by_age))
#people.sort(key=by_salary
print(people)
print([s.upper() for s in "hello world"])
print([w.strip('.') for w in ['these.','ok.','heelo.']])
sentence="Beautiful is better than ugly"
print(["".join(sorted(word ,key=lambda x : x.lower())) for word in sentence.split()])
from random import randrange
print([randrange(1,7) for _ in range(10)])
data = [[1,2],[3,4],[5,6]]
def f():
	output=[]
	for each_list in data:
		for element in each_list:
			output.append(element)
	return output
# Map & Filter
filtered = filter(lambda x: x % 2 == 0, range(10))
results = map(lambda x: 2*x, filtered)
# List comprehension
results = [2*x for x in range(10) if x % 2 == 0]
from groupby import itertools
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"), \
("vehicle", "speed boat"), ("vehicle", "school bus")]
dic={}
f=lambda x: x[0]
for key,group in groupby(sorted(things,key=f),f):
	dic[key]=list(group)
dic'''
import heapq
numbers =[1,4,2,100,171,18,8,5]
print(heapq.nlargest(4,numbers))
print(heapq.nsmallest(4,numbers)) 
people=[
        {'firstname':'John','lastname':'Doe','age':33},
        {'firstname':'Jane','lastname':'Doe','age':25},
        {'firstname':'Janie','lastname':'Doe','age':18},
        {'firstname':'Jane','lastname':'Roe','age':22},
        {'firstname':'Johnny','lastname':'Doe','age':12},
        {'firstname':'John','lastname':'Roe','age':45},
 ]
oldest =heapq.nlargest(2,people,key=lambda s:s['age'])
print(oldest)
youngest =heapq.nsmallest(2,people,key=lambda s:s['age'])
print(youngest)
heapq.heapify(numbers)
print(numbers)
heapq.heappop(numbers)
print(numbers)
heapq.heappop(numbers)
print(numbers)