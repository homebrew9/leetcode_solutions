class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def solve(arr, s):
            if s == '':
                self.res = max(self.res, len(arr))
                print(f'\tres, arr = {self.res}, {arr}')
                return
            for i in range(len(s)):
                chunk = s[:i+1]
                if chunk not in arr:
                    solve(arr + [chunk], s[i+1:])
        self.res = 0
        solve([], s)
        return self.res

# Main section
for s in [
            #'ababccc',
            #'aba',
            #'aa',
            #'aaa',
            #'aaaa',
            #'aaaaa',
            #'aaaaaa',
            'aaaaaaaaaaaaaaaa',
            #'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.maxUniqueSplit(s)
    print(f'r = {r}')
    print('===================')


