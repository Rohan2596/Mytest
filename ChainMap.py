import collections 
dic1={'a':1,'b':2}
dic2={'b':3,'c':4}
dic3={'f':5}
chain =collections.ChainMap(dic1,dic2)
print("Chain.maps",chain.maps)
print("chain.keys",list(chain.keys()))
print("chain.values",list(chain.values()))
chain1=chain.new_child(dic3)
print("chain with added on",chain1)