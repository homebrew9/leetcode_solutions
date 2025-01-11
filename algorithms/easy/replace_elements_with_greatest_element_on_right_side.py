from typing import List

#class Solution:
#    def replaceElements(self, arr: List[int]) -> List[int]:
#        prev_max = -1
#        for i in range(len(arr)-1, -1, -1):
#            if i == len(arr) - 1:
#                prev_max = max(prev_max, arr[i])
#                arr[i] = -1
#            else:
#                temp = arr[i]
#                arr[i] = prev_max
#                prev_max = max(prev_max, temp)
#        return arr

#class Solution:
#    def replaceElements(self, arr: List[int]) -> List[int]:
#        prev_max = -1
#        for i in range(len(arr)-1, -1, -1):
#            temp = arr[i]
#            if i == len(arr) - 1:
#                arr[i] = -1
#            else:
#                arr[i] = prev_max
#            prev_max = max(prev_max, temp)
#        return arr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = -1 if i == len(arr) - 1 else prev_max
            prev_max = max(prev_max, temp)
        return arr

# Main section
for arr in [
              [17,18,5,4,6,1],
              [400],
              [1,2,3,4,5,6,7],
              [7,6,5,4,3,2,1],
              [1,1,1,1,1,1],
              [23,37,23,37,23,37],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.replaceElements(arr)
    print(f'r = {r}')
    print('===========================')

