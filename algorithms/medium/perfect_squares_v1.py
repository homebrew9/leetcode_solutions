from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, n+1) if i*i <= n]
        #print(f'\tsquares = {squares}')
        dq = deque()
        vis = set()
        dq.append(0)
        vis.add(0)
        step = 0
        while dq:
            #print(f'\tstep, dq = {step}, {dq}')
            size = len(dq)
            for i in range(size):
                cur = dq[0]
                #print(f'\t\tcur = {cur}')
                if cur == n:
                    return step
                for sq in squares:
                    tmp = cur + sq
                    if tmp not in vis:
                        dq.append(tmp)
                        vis.add(tmp)
                dq.popleft()
            step += 1
        return -1

# Main section
for n in [
            1,
            12,
            13,
            1234,
            10000,
            778,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.numSquares(n)
    print(f'r = {r}')
    print('===============')

