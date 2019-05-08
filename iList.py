from collections import UserList

class iList(UserList):

    def __init__(self, initlist=[]):
        # data in 'self.data'
        if type(initlist) == range:
            d = []
            for item in initlist:
                d.append(item)
            return super().__init__(d)
        return super().__init__(initlist.copy()) # append used for: range -> list

    def insert(self, index, item):
        cpy = self.data.copy()
        cpy.insert(index, item)
        return cpy

    def pop(self, index):
        cpy = self.data.copy()
        cpy.pop(index)
        return cpy

    def clear(self):
        return iList()

    def sort(self, key=None, reverse=False):
        cpy = self.data.copy()
        cpy.sort(key, reverse)
        return cpy

    def reverse(self):
        cpy = self.data.copy()
        cpy.reverse()
        return cpy

    

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

    