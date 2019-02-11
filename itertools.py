import itertools
'''a=[1,2,3,4,5,6]
b=list(itertools.combinations(a,2))
print(b)
c=list(itertools.combinations(a,3))
print(c)
##itertools dropwhile enables to take items form sequence after a conditions first becomes False
def is_even(x):
	return x %2==0
def is_odd(x):
	return x %2!=0 
lst=[0,2,4,6,8,12,10,12,13,5,62,8,10]
result=list(itertools.dropwhile(is_even,lst))

print(result)
result1=list(itertools.dropwhile(is_odd,lst))
print(result1)'''
''''from itertools import zip_longest
a=[i for i in range(5)]
b=['a','b','c','d','e','f','g','h']
for i in zip_longest(a,b):
	x,y=i
	print(x,y)
results=fetch_paged_results()
limit =20
for data in itertools.islice(results,limit):
	print(data)'''
'''lst=[("a",5,6),("b",2,4),("a",2,5),("c",2,6)]
def testGroupby(lst):
	groups=itertools.groupby(lst,key=lambda x:x[1] )
	for key,group in groups:
		print(key,list(group))
testGroupby(lst)
import itertools as it
import operator
print(list(it.accumulate([1,2,3,4])))
print(list(it.accumulate([1,2,3,4,5],func=operator.mul)))
print(list(it.cycle('ROH')))
for x,y in itertools.product(xrange(10),xrange(10)):
	print(x,y)
'''
import dis
def hello():
	print("hello,world")
print(dis.dis(hello))