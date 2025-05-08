# Python’s OrderedDict
from collections import OrderedDict

od:OrderedDict[str, int] = OrderedDict()
od["one"] = 1
od["two"] = 2
od["three"] = 3

print(od)

# iterable of items as an argument
od= OrderedDict([("one", 1), ("two", 2), ("three", 3)])
print(od)

letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
print(letters)

# Keyword Arguments
od:OrderedDict[str, int] = OrderedDict(one=1, two=2, three=3)
print(od)

# use .fromkeys() methods
keys = ["one", "two", "three"]
od = OrderedDict.fromkeys(keys, 0)
print(od)

#Managing Items in an OrderedDict
od:OrderedDict[str, int] = OrderedDict(one=1, two=2, three=3)
print(od)
od["four"] = 4
print(od)

# delete item
del od["one"]
print(od)

#update item
od["one"] = 1
print(od)

# update() method
od.update(two = 22)
print(od)

# Iterating Over an OrderedDict

for key in od:
    print(key, ":", od[key])


# Iterate over the items using .items()
for key, value in od.items():
    print(key, ":", value)


# Iterate over the keys using .keys()
for key in od.keys():
    print(key, ":", od[key])


# Iterate over the values using .values()
for value in od.values():
    print(value)

# Iterate over the keys directly with reversed class
for key in reversed(od):
    print(key, ":", od[key])


# moving item to end using move_to_end() method
print(od)
od.move_to_end("two")
print(od)

print(od)
od.move_to_end("two", last=True)
od.move_to_end("two", last=False)
print(od)

#Removing Items With .popitem()
print(od)
print(od.popitem(last=False))
print(od)

# Equality Comparison in Python Dictionary Order
od1:OrderedDict[str, int] = (
    OrderedDict(one=1, two=2, three=3))

od2:OrderedDict[str, int] = (
    OrderedDict(one=1, two=2, three=3))

od3:OrderedDict[str, int] = (
    OrderedDict(one=1, three=3,two=2))

print(od1 == od2)
print(od1 == od3)
print(od2 == od3)

# Equality Comparison in Python Dictionary

od1:dict[str, int] = (
    dict(one=1, two=2, three=3))

od2:dict[str, int] = (
    dict(one=1, two=2, three=3))

od3:dict[str, int] = (
    dict(one=1, three=3,two=2))

print(od1 == od2)
print(od1 == od3)

