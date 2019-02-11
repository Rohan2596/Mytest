'''import collections 
dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
dic3={'f':5}
chain =collections.ChainMap(dic1,dic2)
print("Chain.maps",chain.maps)
print("chain.keys",list(chain.keys()))
print("chain.values",list(chain.values()))
chain1=chain.new_child(dic3)
print("chain with added on",chain1)'''
import collections
dict1={'apple':1,'banana':2}
dict2={'coconut':1,'date':1,'apple':3}
combined_dict =collections.ChainMap(dict1,dict2)
reversed_ordered_dict=collections.ChainMap(dict2,dict1)
print("combined_dict:")
for k,v in combined_dict.items():
	print(k,v)
print("reversed_ordered_dict:")
for i,j in reversed_ordered_dict.items():
	print(i,j)