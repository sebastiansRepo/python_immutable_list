from collections import UserList

class iList(UserList):

    def __init__(self, initlist=[]):
        # data in 'self.data'
        return super().__init__(initlist)

    def __repr__(self):
        return super().__repr__()

    def __eq__(self, value):
        return super().__eq__(value)

    def __ge__(self, other):
        return super().__ge__(other)

    def __gt__(self, other):
        return super().__gt__(other)

    def __le__(self, other):
        return super().__le__(other)

    def __ne__(self, value):
        return super().__ne__(value)

    def __lt__(self, other):
        return super().__lt__(other)


class iList_Test():
    
    pass
    
x = iList()
x.append(1)
print(x)