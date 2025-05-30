from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # Recursive solution
        def solve(i, total):
            if i >= N:
                return arr[-1]
            if total <= arr[i] * (N - i):
                replacement_amount = total / (N - i)
                if replacement_amount - int(replacement_amount) == 0.5:
                    return int(replacement_amount)
                return round(replacement_amount)
            return solve(i+1, total - arr[i])
        N = len(arr)
        arr.sort()
        return solve(0, target)

# Main section
for arr, target in [
                      ([4,9,3], 10),
                      ([2,3,5], 10),
                      ([60864,25176,27249,21296,20204], 56803),
                      ([2,2], 3),
                      ([2,3,5], 11),
                      ([48772,52931,14253,32289,75263], 40876),
                   ]:
    print(f'arr, target = {arr}, {target}')
    sol = Solution()
    r = sol.findBestValue(arr, target)
    print(f'r = {r}')
    print('========================================')






