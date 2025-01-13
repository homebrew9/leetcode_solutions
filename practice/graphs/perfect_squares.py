from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        dq = deque()
        seen = set()
        squares = list()
        i = 0
        while i*i <= n:
            squares.append(i*i)
            dq.append(i*i)
            seen.add(i*i)
            i += 1
        steps = 1
        while dq:
            size = len(dq)
            for _ in range(size):
                cur = dq.popleft()
                if cur == n:
                    return steps
                for sq in squares:
                    if cur + sq <= n and cur + sq not in seen:
                        seen.add(cur+sq)
                        dq.append(cur+sq)
            steps += 1

# Main section
for n in [
            12,
            13,
            100,
            1234,
            9999,
            10000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.numSquares(n)
    print(f'r = {r}')
    print('================')


