# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap_count(original):
            orig = original[:]
            target = sorted(original)
            pos = {v: i for i, v in enumerate(original)}
            swaps = 0
            for i in range(len(original)):
                if original[i] != target[i]:
                    swaps += 1
                    cur_pos = pos[target[i]]
                    pos[original[i]] = cur_pos
                    original[cur_pos] = original[i]
            #arr1 = [(v, i) for i, v in enumerate(arr)]
            #idx = [i for _, i in sorted(arr1)]
            #swaps = 0
            #for i in range(len(idx)):
            #    if idx[i] != i:
            #        j = idx[i]
            #        idx[i], idx[j] = idx[j], idx[i]
            #        swaps += 1
            #print(swaps, orig)
            return swaps
        dq = deque()
        dq.append(root)
        res = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res += min_swap_count([x.val for x in dq])
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap_count(arr):
            #orig = original[:]
            #target = sorted(original)
            #pos = {v: i for i, v in enumerate(original)}
            #swaps = 0
            #for i in range(len(original)):
            #    if original[i] != target[i]:
            #        swaps += 1
            #        cur_pos = pos[target[i]]
            #        pos[original[i]] = cur_pos
            #        original[cur_pos] = original[i]
            orig = arr[:]
            arr1 = [(v, i) for i, v in enumerate(arr)]
            idx = [i for _, i in sorted(arr1)]
            swaps = 0
            for i in range(len(idx)):
                while idx[i] != i:
                    j = idx[i]
                    idx[i], idx[j] = idx[j], idx[i]
                    swaps += 1
            print(swaps, orig)
            return swaps
        dq = deque()
        dq.append(root)
        res = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res += min_swap_count([x.val for x in dq])
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap_count(arr):
            # We use Cycle Sort to determine the minimum number of
            # swaps to sort the array arr.
            sorted_arr = sorted(arr)
            pos = {v: i for i, v in enumerate(sorted_arr)}
            swaps = 0
            for i in range(len(arr)):
                while (j := pos[arr[i]]) != i:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
            return swaps
        dq = deque()
        dq.append(root)
        res = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res += min_swap_count([x.val for x in dq])
        return res


