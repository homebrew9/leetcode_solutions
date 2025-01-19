from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        arr = list()
        cnt = 0
        currSum = 0
        banned.sort()
        N = len(banned)
        for i in range(1, n+1):
            found = False
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) // 2
                if banned[mid] == i:
                    found = True
                    break
                elif banned[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1
            if not found:
                currSum += i
                if currSum <= maxSum:
                    cnt += 1
                    arr.append(i)
            if currSum > maxSum:
                break
        print(f'\tarr = {arr}')
        return cnt

# Main section
for banned, n, maxSum in [
                            ([1,6,5], 5, 6),
                            ([1,2,3,4,5,6,7], 8, 1),
                            ([11], 7, 50),
                            ([176,36,104,125,188,152,101,47,51,65,39,174,29,55,13,138,79,81,175,178,42,108,24,80,183,190,123,20,139,22,140,62,58,137,68,148,172,76,173,189,151,186,153,57,142,105,133,114,165,118,56,59,124,82,49,94,8,146,109,14,85,44,60,181,95,23,150,97,28,182,157,46,160,155,12,67,135,117,2,25,74,91,71,98,127,120,130,107,168,18,69,110,61,147,145,38], 3016, 240),
                         ]:
    print(f'banned, n, maxSum = {banned}, {n}, {maxSum}')
    sol = Solution()
    r = sol.maxCount(banned, n, maxSum)
    print(f'r = {r}')
    print('================')

