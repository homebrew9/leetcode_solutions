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
    def findBestValue_1(self, arr: List[int], target: int) -> int:
        def sign(x):
            if x < 0: return -1
            if x > 0: return 1
            return 0
        N = len(arr)
        arr.sort()
        #print(arr)
        res = 0
        diff, diff_abs, diff_sign = None, None, None
        prev_diff_abs, prev_diff_sign = None, None
        while res <= max(arr):
            total = sum([res if v > res else v for v in arr])
            # ==============================================
            diff      = target - total
            diff_abs  = abs(diff)
            diff_sign = sign(diff)
            # ==============================================
            #print(f'\tres, diff, diff_abs, diff_sign = {res}, {diff}, {diff_abs}, {diff_sign}')
            if prev_diff_sign and diff_sign != prev_diff_sign:
                if prev_diff_abs <= diff_abs:
                    return res - 1
                if diff_abs < prev_diff_abs:
                    return res
                break
            # ==============================================
            prev_diff_abs  = diff_abs
            prev_diff_sign = diff_sign
            # ==============================================
            #print(f'\tres, diff, diff_abs, diff_sign, prev_diff_abs, prev_diff_sign = {res}, {diff}, {diff_abs}, {diff_sign}, {prev_diff_abs}, {prev_diff_sign}')
            res += 1
        return min(max(arr), res)

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
    r1 = sol.findBestValue_1(arr, target)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('========================================')

