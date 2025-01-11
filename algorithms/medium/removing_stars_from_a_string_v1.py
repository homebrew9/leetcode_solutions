class Solution:
    def removeStars(self, s: str) -> str:
        arr = list()
        for ch in s:
            if ch == '*':
                arr.pop()
            else:
                arr.append(ch)
        return ''.join(arr)

# Main section
sol = Solution()
for s in [
            #'leet**cod*e',
            #'erase*****',
            #'a*b*c*d*',
            'abc*def*ghi****jklmnop*qrstuv**xyz',
         ]:
    print(f's = {s}')
    r = sol.removeStars(s)
    print(f'r = {r}')
    print('======================')


