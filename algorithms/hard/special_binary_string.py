class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def solve(a, b):
            if a > b:
                return ''
            curr = 0
            is_new_segment = False
            arr = list()
            for i in range(a, b+1):
                if not is_new_segment:
                    is_new_segment = True
                    p = i
                    curr = 1 if s[i] == '1' else -1
                else:
                    curr = curr + 1 if s[i] == '1' else curr - 1
                    if curr == 0:
                        q = i
                        tmp = s[p] + solve(p+1, q-1) + s[q] # type: ignore
                        arr.append(tmp)
                        is_new_segment = False
            return ''.join(sorted(arr, reverse=True))
        N = len(s)
        res = solve(0, N-1)
        return res

# Main section
for s in [
            '101101001100',
            '11011000',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.makeLargestSpecial(s)
    print(f'r = {r}')
    print('=================================================')
 








