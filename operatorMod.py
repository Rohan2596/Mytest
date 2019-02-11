from itertools import groupby
from operator import itemgetter
adict={'a':1,'b':5,'c':1}
print(adict((i,dict(v)) for i, v in groupby(adict.items(),itemgetter(1))))
alist_of_tuples=[(5,2),(1,3),(2,2)]
print(sorted(alist_of_tuples,keys=itemgetter(1,0)))
       