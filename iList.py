from collections import UserList

class iList(UserList):

    def __init__(self, initlist=[]):
        # data in 'self.data'
        if type(initlist) == range:
            d = []
            for item in initlist:
                d.append(item)
            return super().__init__(d)
        return super().__init__(initlist)

    def _immutable_decorator(func):
        def f(self, *args, **kwargs):
            cpy = cpy = self.data.copy()
            method = getattr(cpy, func.__name__)
            method(*args, **kwargs)
            return cpy
        return f
    
    @_immutable_decorator
    def insert(self, i, item):
        return super().insert(i, item)

    @_immutable_decorator
    def pop(self, i):
        return super().pop(i)

    @_immutable_decorator
    def sort(self, *args, **kwds):
        return super().sort(*args, **kwds)

    @_immutable_decorator
    def reverse(self):
        return super().reverse()

    def append(self, item, flat=True):
        # flat -> [1,2,3].append([5,6]) == [1,2,3,5,6]; [1,2,3].append((5,6)) == [1,2,3,5,6]
        # flat false -> [1,2,3].append([5,6]) == [1,2,3,[5,6]]
        cpy = self.data.copy()
        if type(item) == list or type(item) == tuple or type(item) == set or type(item) == range:
            if flat:
                for i in item:
                    cpy.append(i)
                return cpy
            else:
                cpy.append(0) # make list bigger
                cpy[-1] = item
                return cpy
        cpy.append(item)
        return cpy

    def remove(self, item):
        cpy = self.data.copy()
        cpy.remove(item)
        return cpy

    def __add__(self, other):
        return self.append(other)


    def __sub__(self, other):
        return self.remove(other)


    def clear(self):
        return iList()