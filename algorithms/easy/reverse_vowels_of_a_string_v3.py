class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        arr = list(s)
        left, right = 0, len(arr) - 1
        while left < right:
            print(f'\tleft, right = {left}, {right}')
            if not arr[left] in vowels:
                left += 1
                continue
            print(f'\tafter 1st if...')
            while not arr[right] in vowels:
                right -= 1
            print(f'\tafter while, right = {right}')
            if left >= right:
                break
            arr[left], arr[right] = arr[right], arr[left]
            print(f'\tafter swap, arr = {arr}')
            left += 1
            right -= 1
        return ''.join(arr)

# Main section
for s in [
            'leetcode',
            'pAqErIsOtUuavew',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reverseVowels(s)
    print(f'r = {r}')
    print('===============')

