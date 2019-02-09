s={1,2}
i=iter(s)
a=next(i)
b=next(i)
#c=next(i)
l1=list(s)
l2=[a*2 for a in s if a > 2]
print(l2)
a, iterable