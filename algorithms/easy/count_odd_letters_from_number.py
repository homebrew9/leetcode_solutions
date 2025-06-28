from collections import defaultdict

class Solution:
    def countOddLetters(self, n: int) -> int:
        hsh = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
               6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
        cntr = defaultdict(int)
        while n > 0:
            q, r = divmod(n, 10)
            for ch in hsh[r]:
                cntr[ch] += 1
            n = q
        return sum([v % 2 == 1 for v in cntr.values()])

# Main section
for n in [
            41,
            20,
            1000000000,
            899834798,
            173720093,
            3599,
            99832382,
            217,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countOddLetters(n)
    print(f'r = {r}')
    print('=======================')













