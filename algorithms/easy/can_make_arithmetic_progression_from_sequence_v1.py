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
        i = 0
        while True:
            #print(f'\ti, arr = {i}, {arr}')
            if i >= N:
                break
            curr = arr[i]
            if (curr - min_value) % diff != 0:
                return False
            pos = (curr - min_value)//diff
            if i != pos:
                # Special case 3 - if there are duplicates at this point, then it's not an AP
                #                  since diff > 0
                if arr[i] == arr[pos]:
                    return False
                # Swap the elements
                arr[i], arr[pos] = arr[pos], arr[i]
            else:
                i += 1
        #print(f'\tarr = {arr}')
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


