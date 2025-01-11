from typing import List
from sortedcontainers import SortedList

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.sl = SortedList(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.sl.add(val)
        return self.sl[-k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Example 1:
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# 
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8


# Main section
for cmd, val, out in [
                        (
                           ['KthLargest', 'add', 'add', 'add', 'add', 'add'],
                           [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
                           [None, 4, 5, 5, 8, 8],
                        ),
                     ]:
    print('==================================')
    print(f'cmd, val, out = {cmd}, {val}, {out}')
    for c, v, o in zip(cmd, val, out):
        if c == 'KthLargest':
            k, nums = v
            obj = KthLargest(k, nums)
            print(f'obj = {obj}')
        elif c == 'add':
            r = obj.add(v[0])
            print(f'r, o = {r}, {o}')
        print('~~~~~')


