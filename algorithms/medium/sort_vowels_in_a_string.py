from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        it = iter(sorted([ch for ch in s if ch in vowels]))
        return ''.join([it.__next__() if ch in vowels else ch for ch in s])
    def sortVowels_1(self, s: str) -> str:
        # Counting Sort
        sortedVowels = 'AEIOUaeiou'
        hsh = defaultdict(int)
        for ch in s:
            if ch in sortedVowels:
                hsh[ch] += 1
        ans = ''
        j = 0
        for ch in s:
            if ch not in sortedVowels:
                ans += ch
            else:
                while j < len(sortedVowels) and hsh[sortedVowels[j]] == 0:
                    j += 1
                ans += sortedVowels[j]
                hsh[sortedVowels[j]] -= 1
        return ans

# Main section
for s in [
            'lEetcOde',
            'lYmpH',
         ]:
    print(f's  = {s}')
    sol = Solution()
    r = sol.sortVowels(s)
    r1 = sol.sortVowels_1(s)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===================')







































