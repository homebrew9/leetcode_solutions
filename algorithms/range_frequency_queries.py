import collections
from bisect import bisect_right, bisect_left
from typing import List

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.d = collections.defaultdict(list)
        for i in range(len(arr)):
            self.d[arr[i]].append(i)  # store the indices of a number as map
        print(self.d)
            
    # difference between right and left gives the frequency
    def query(self, left: int, right: int, value: int) -> int:
        print('=========')
        print(f'left, right, value = {left}, {right}, {value}')
        print(bisect_right(self.d[value], right))
        print(bisect_left(self.d[value], left))
        return bisect_right(self.d[value], right) - bisect_left(self.d[value], left)

# Main section
# Your RangeFreqQuery object will be instantiated and called as such:
arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
print(f'arr = {arr}')
obj = RangeFreqQuery(arr)
param_1 = obj.query(1, 2, 4)
param_2 = obj.query(0, 11, 33)
print(f'param_1 = {param_1}')
print(f'param_2 = {param_2}')

