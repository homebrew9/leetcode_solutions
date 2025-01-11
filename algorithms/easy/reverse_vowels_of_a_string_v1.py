class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = ['a','e','i','o','u','A','E','I','O','U']
        arr = list(s)
        left = 0
        right = len(arr) - 1
        while True:
            while left < len(arr) and not arr[left] in lst:
                left += 1
                #print(f'\tleft = {left}')
            while right >= 0 and not arr[right] in lst:
                right -= 1
                #print(f'\tright = {right}')
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)

# Main section
for s in [
            'hello',
            'leetcode',
            'aeiou',
            'cauliflower',
            'rhythm',
            'a',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reverseVowels(s)
    print(f'r = {r}')
    print('===========================')

