# UserDict in Python | Collection Module
from collections import UserDict

class MyPreferences(UserDict):
    def __setitem__(self, key, value):
        print(f"{key} set..")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        print(f"{key} accessed..")
        return super().__getitem__(key)


prefs = MyPreferences()
prefs['Theme'] = 'Dark'
prefs.setdefault("Font", 25)
print(prefs['Theme'])
print(prefs.get("Theme"))





