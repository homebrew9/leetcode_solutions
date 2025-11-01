from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def solve(x):
            cnt = 1
            prev = price[0]
            for i in range(1, N):
                if price[i] - prev >= x:
                    prev = price[i]
                    cnt += 1
                    if cnt >= k:
                        break
            return cnt >= k
        N = len(price)
        price.sort()
        left, right = 0, max(price)
        while left <= right:
            mid = (left + right) // 2
            is_valid = solve(mid)
            if not is_valid:
                right = mid - 1
            else:
                left = mid + 1
        return right

# Main section
for price, k in [
                   ([13,5,1,8,21,2], 3),
                   ([1,3,1], 2),
                   ([7,7,7,7], 2),
                ]:
    print(f'price, k = {price}, {k}')
    sol = Solution()
    r = sol.maximumTastiness(price, k)
    print(f'r = {r}')
    print('=====================')

