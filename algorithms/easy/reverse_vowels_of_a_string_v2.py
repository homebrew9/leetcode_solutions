class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        hsh = dict([(i,v) for i,v in enumerate(arr) if v in 'aeiouAEIOU'])
        for a, b in zip(list(hsh.keys())[::-1], list(hsh.values())):
            arr[a] = b
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


