class Solution:
    def reverseVowels(self, s: str) -> str:
        lst_vowels = ['a','e','i','o','u','A','E','I','O','U']
        arr = list(s)
        left = 0
        right = len(s) - 1
        while True:
            while left <= right and not s[left] in lst_vowels:
                left += 1
            while right >= 0 and not s[right] in lst_vowels:
                right -= 1
            if left >= right:
                break
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)

# Main section
sol = Solution()
for s in [
            'leetcode',
            'abcdefghijklmnopqrstuvwxyz',
            'hello',
            'bcdfghjklmnpqrstvwxyz',
            'aeiouAEIOU',
            'thequickbrownfoxjumpsoverthelazydog',
         ]:
    print(f's = {s}')
    r = sol.reverseVowels(s)
    print(f'r = {r}')
    print('======================')

