from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i, zero_count):
            print(f'=====\n\ti, zc; dist = {i}, {zero_count}; {distribute}')
            # If there are not enough cookies remaining, return INF
            # as it leads to an invalid distribution
            if n - i < zero_count:
                return float('inf')

            # After distributing all cookies, return the unfairness
            # of this distribution
            if i == n:
                return max(distribute)

            # Try to distribute the i-th cookie to each child, and update
            # answer as the minimum unfairness in these distributions
            answer = float('inf')
            for j in range(k):
                print(f'\t\tj = {j}')
                if distribute[j] == 0:
                    zero_count -= 1
                # ==================================================
                distribute[j] += cookies[i]
                # Recursively distribute the next cookie
                answer = min(answer, dfs(i+1, zero_count))
                # Backtrack step
                distribute[j] -= cookies[i]
                # ==================================================
                if distribute[j] == 0:
                    zero_count += 1
            return answer
        
        distribute = [0 for _ in range(k)]
        n = len(cookies)
        return dfs(0, k)

# Main section
for cookies, k in [
                     #([8,15,10,20,8], 2),
                     #([6,1,3,2,2,4,1,2], 3),
                     #([1,2,1], 2),
                     ([1,2], 2),
                  ]:
    print(f'cookies, k = {cookies}, {k}')
    sol = Solution()
    r = sol.distributeCookies(cookies, k)
    print(f'r = {r}')
    print('================')

