# Collection Module- > UserList class

from collections import UserList
from collections.abc import MutableSequence

def validate(val):
    if val <= 100:
        return True
    else:
        return False

lst:list = []
val = int(input("Enter value:"))
if validate(val):
    lst.append(val)

print(lst)

from collections.abc import MutableSequence
# subclass inherits built-in MutableSequence type from abc
class ValidatedList(MutableSequence):

    def __init__(self, initial=None):
        self._data = []
        if initial:
            for item in initial:
                self.append(item)  # Use append to apply validation

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed.")
        if not (value <= 100):
            raise ValueError("Value must be less then 100.")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self.validate(value)
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, index, value):
        self.validate(value)
        self._data.insert(index, value)

    def append(self, value):
        self.validate(value)
        self._data.append(value)

    def __str__(self):
        return str(self._data)

# 🧪 Test
vl = ValidatedList([1, 50])
vl.append(99)
vl[0] = 60
print(vl)


# subclass inherits built-in list type
class ValidatedListV1(list):


    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed.")
        if not (value <= 100):
            raise ValueError("Value must be less then 100.")

    def append(self, value):
        self.validate(value)
        super().append(value)

    def insert(self, index, value):
        self.validate(value)
        super().insert(index, value)


    def extend(self, iterable):
        for item in iterable:
            self.validate(item)
        super().extend(iterable)

v1 = ValidatedListV1([10, 20])
v1.append(90)
v1.insert(1, 50)
v1[0] = 75
print(vl)


from collections import UserList

class ValidatedUserList(UserList):

    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError("Only integers are allowed.")
        if not (0 <= value <= 100):
            raise ValueError("Value must be between 0 and 100.")

    def append(self, item):
        self.validate(item)
        self.data.append(item)

    def insert(self, index, item):
        self.validate(item)
        self.data.insert(index, item)

    def __setitem__(self, index, item):
        if isinstance(index, slice):
            for val in item:
                self.validate(val)
        else:
            self.validate(item)
        self.data.__setitem__(index, item)

    def extend(self, other):
        for item in other:
            self.validate(item)
        self.data.extend(other)


v2 = ValidatedUserList([10, 20])
v2.append(30)
v2.insert(1, 50)
v2[0] = 75
v2[1:3] = [35, 40]
v2.extend([90, 99])
print(v2)  # Output: [75, 35, 40, 90, 99]


# Audit Log for application using UserList
from collections import UserList

class AuditList(UserList):
    def __init__(self, iterable=None):
        super().__init__(iterable or [])
        self.log = []

    def append(self, item):
        self.log.append(f"Appended: {item}")
        self.data.append(item)

    def remove(self, item):
        self.log.append(f"Removed: {item}")
        self.data.remove(item)

    def get_log(self):
        return self.log


a1 = AuditList([1, 2])
a1.append(3)
a1.remove(1)

print(a1)
print(a1.get_log())
