#
# Completely wrong approach!! Don't go through all integers and then find out if they
# are palindromes and divisible by k! That will TLE!! Find out only the palindromes
# first and then figure out how many numbers would be there with those digits!
#
import itertools
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def is_palindrome(s, n):
            cntr = Counter(s)
            even_frequencies = 0
            odd_frequencies = 0
            for v in cntr.values():
                if v % 2 == 0:
                    even_frequencies += 1
                else:
                    odd_frequencies += 1
            if n % 2 == 0:
                return odd_frequencies == 0
            if n % 2 == 1:
                return odd_frequencies == 1
        def is_good(s, n, k):
            if len(str(int(s))) != n:
                return False
            if int(s) == 0:
                return False
            if s == s[::-1] and int(s) % k == 0:
                self.good.add(s)
                return True
            seen = set()
            bln = True
            for item in itertools.permutations(s, n):
                num = ''.join(item)
                if len(str(int(num))) != n:
                    return False
                if num in seen:
                    continue
                seen.add(num)
                if num == num[::-1] and int(num) % k != 0:
                    print(f'Inside is_good; s = {s}. Is_palindrome but not divisible: {num}')
                if num == num[::-1] and int(num) % k == 0:
                    self.good.add(num)
                    #return True
                    bln = bln and True
            return bln
            
        def is_divisible(s, k):
            return int(s) % k == 0
        def solve(s, n):
            #print(f'\ts, n = {s}, {n}')
            if len(s) == n:
                #print(f'\t\tInside len(s) == n')
                #if is_palindrome(s, n) and is_divisible(s, k):
                if is_good(s, n, k):
                    print(f'\t\t\t{s} is palindrome and divisible')
                    self.cnt += 1
                return
            nums = '123456789' if s == '' else '0123456789'
            #nums = '0123456789'
            for ch in nums:
                solve(s + ch, n)
            
        self.cnt = 0
        self.good = set()
        solve('', n)
        print(f'self.cnt = {self.cnt}')
        #return self.cnt
        return len(self.good)


# Main section
for n, k in [
               (5, 6),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.countGoodIntegers(n, k)
    print(f'r = {r}')
    print('================')


