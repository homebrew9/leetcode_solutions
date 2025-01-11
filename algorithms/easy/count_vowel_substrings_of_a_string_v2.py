#
# One pass, no sliding window, O(n)
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/discuss/1563888/Python-One-pass-no-sliding-window-O(n)
#
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -2 for v in vowels}
        for i, x in enumerate(word):
            if x not in vowels:
                last_consonant = i
            else:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values())-last_consonant, 0)
            print(f'\ti, x, lc, lsv, ans = {i}, {x}, {last_consonant}, {last_seen_vowels}, {ans}')
        print(f'ans = {ans}')
        return ans

# Main section
for word in [
               #'aeiouua',
               #'unicornarihan',
               #'cuaieuouac',
               #'cuaieoxyz',
               #'xaeiouaeiy',
               #'xaeiouaaiy',
               'xaeiouaeiouaeiou',
               #'poazaeuioauoiioaouuouaui',
               #'ughspuuoaaaoieiuiaoiuee',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.countVowelSubstrings(word)
    print(f'r = {r}')
    print('=====================')

