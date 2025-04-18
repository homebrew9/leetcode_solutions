class Solution:
    def countAndSay(self, n: int) -> str:
        # Iterative solution
        for j in range(n):
            if j == 0:
                res = '1'
                continue
            tmp = ''
            ch, freq = None, 0
            for i, v in enumerate(res):
                if i == 0 or v != res[i-1]:
                    if freq > 0:
                        tmp += f'{freq}{ch}'
                    freq = 1
                    ch = v
                else:
                    freq += 1
            tmp += f'{freq}{ch}'
            res = tmp
        return res
    def countAndSay_1(self, n: int) -> str:
        # Recursive algorithm - use the recursive definitions from the problem description.
        def rle(s):
            res = ''
            ch, freq = None, 0
            for i, v in enumerate(s):
                if i == 0 or v != s[i-1]:
                    if freq > 0:
                        res += f'{freq}{ch}'
                    freq = 1
                    ch = v
                else:
                    freq += 1
            res += f'{freq}{ch}'
            return res
        def count_n_say(n):
            if n == 1:
                return '1'
            return rle(count_n_say(n - 1))
        return count_n_say(n)

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            10,
            15,
            20,
            25,
            30,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countAndSay(n)
    r1 = sol.countAndSay_1(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('=================')

