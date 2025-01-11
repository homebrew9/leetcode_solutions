# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(lst):
            for i in lst:
                if i.isInteger():
                    self.res.append(i.getInteger())
                else:
                    flatten(i.getList())

        self.res = list()
        flatten(nestedList)
        self.ptr = -1
        self.size = len(self.res)
    
    def next(self) -> int:
        return self.res[self.ptr]
    
    def hasNext(self) -> bool:
        self.ptr += 1
        if self.ptr >= self.size:
            return False
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
"""

def flatten(nl):
    def iterate(lst):
        for i in lst:
            if type(i) == int:
                res.append(i)
            elif type(i) == list:
                iterate(i)
    res = list()
    iterate(nl)
    return res

for nl in [
             [[1,1],2,[1,1]],
             [1,[4,[6]]],
             [[[[[[[[[[[[[[1]]]]]]]]]]]]]],
             [[[[[[[[[[[[[[1],2],3],4],5],6],7],8],9],10],11],12],13],14],
             [1,[2,[3,[4,[5,[6,[7,[8,[9,[10,[11,[12,[13,[14,15],16],17],18],19],20],21],22],23],24],25],26],27],28],
          ]:
    print(f'nl = {nl}')
    r = flatten(nl)
    print(f'r = {r}')
    print('=============')

