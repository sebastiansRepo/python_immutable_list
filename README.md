# Immutable list for python

Having to implement algorithms in python often forces you to copy your lists. 
In addition, I wanted list.append, .remove to return the list itself.

The iList implementation extends collections.UserList: see https://docs.python.org/3/library/collections.html#collections.UserList


## enabling python unit tests in Visual Studio Code
Execute command __Python: Configure Tests__ and select "unittest" -> ". (Root Directory)" -> "_test.py"

for more details: see https://code.visualstudio.com/docs/python/unit-testing#_enable-a-test-framework