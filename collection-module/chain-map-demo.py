# Collection Module- > ChainMap class
import requests


from collections import ChainMap

d1 = {'k1': 1, 'k2': 2}
d2 = {'k2': 15, 'k3': 3}

# creating new ChainMap
chain = ChainMap(d1, d2)
print(chain)

# Accessing elements using keys
print(chain["k1"] )
print(chain.get("k1") )

# Adding a new dictionary to Chain Map
d3 = {'k4': 4}
chain.maps.append(d3)
print(chain)

# .new_child() method.
d3 = {'k4': 4}
chain = chain.new_child(d3)
print(chain)

# Adding a new key value pair
chain['k4'] = 4
print(chain)

# Updating existing key value pair
chain['k2'] = 22
print(chain)
chain['k1'] = 11
print(chain)

# Deleting a key-value pair
del chain['k1']
print(chain)

# Iterating over a ChainMap
for k,v in chain.items():
  print(k,":",v)

# chain.maps
print(chain.maps)
# chain.keys()
print(list(chain.keys()))
# chain.values()
print(list(chain.values()))


# Chainmap.copy()
print(chain.copy())

# reversing the ChainMap
chain.maps = reversed(chain.maps)
print(list(chain.maps))
