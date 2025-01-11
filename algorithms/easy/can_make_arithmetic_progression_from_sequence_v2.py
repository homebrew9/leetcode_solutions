from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Time Complexity = O(N)
        # Space Complexity = O(1)
        min_value = float('inf')
        max_value = float('-inf')
        N = len(arr)
        for n in arr:
            min_value = min(min_value, n)
            max_value = max(max_value, n)
        # Special case 1 - diff must be an integer
        if (max_value - min_value) % (N-1) != 0:
            return False
        diff = (max_value - min_value)//(N-1)
        # Special case 2 - if diff is zero, all elements must be identical
        if diff == 0:
            if len(set(arr)) == 1:
                return True
            else:
                return False
        # At this point, diff > 0 so all elements must be different.
        # We do in-place swaps in arr.
        for i, v in enumerate(arr):
            # Determine the true position of v
            if (v - min_value) % diff != 0:
                return False
            pos = (v - min_value)//diff
            while i != pos:
                # Swap elements at i and pos if they are different
                if arr[i] == arr[pos]:
                    return False
                arr[i], arr[pos] = arr[pos], arr[i]
                if (arr[i] - min_value) % diff != 0:
                    return False
                pos = (arr[i] - min_value)//diff
        return True


# Main section
for arr in [
              [5,9,1,7,3],
              [5,9,1,3,3],
              [18,-4,-20,-12,2,14,-18,20,16,8,-14,-16,6,-2,0,-10,12,-6,4,10,-8],
              [18,-4,-20,-12,2,14,-18,20,16,8,-14,-16,6,-2,0,-10,12,6,4,10,-8],
              [7,7,7,7,7,7,7],
              [7,7,7,8,7,7,14],
              [2,10,7,8,3],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.canMakeArithmeticProgression(arr)
    print(f'r = {r}')
    print('===========================')



