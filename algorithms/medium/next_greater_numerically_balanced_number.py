from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while i < 1224445:
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                break
            i += 1
        return i

# Main section
for n in [
            1,
            1000,
            3000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.nextBeautifulNumber(n)
    print(f'r = {r}')
    print('=====================')























