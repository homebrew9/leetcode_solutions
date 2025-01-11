class Solution:
    def numSquares(self, n: int) -> int:
        # The root node is n, and we try to keep reducing a perfect square
        # number from it in each layer. So the next layer nodes are
        # {n - i**2 for i in range(1, int(n**0.5)+1)}. And target leaf node
        # is 0, which indicates n is made up of a number of perfect square
        # numbers and depth is the least number of perfect square numbers.
        # For n = 12, the BFS traverses in the following way:
        # squares = [1,4,9]
        #     
        #            [11,    [2,
        #    [12] ->   8, ->  4,  <== 4 is equal to a square in squares
        #              3]     7,
        #                    10]
        # -------------------------
        #    d=1      d=2    d=3
        #     
        # But this method is slow for n >= 10**9
        #
        squares = [i*i for i in range(1,n+1) if i*i <= n]
        #print(f'\tsquares = {squares}')
        d = 1
        q, nq = set(), set()
        q.add(n)
        while q:
            #print(f'\tq = {q}')
            for node in q:
                for square in squares:
                    if node == square:
                        return d
                    if node < square:
                        break
                    nq.add(node - square)
            q = nq
            nq = set()
            d += 1
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

