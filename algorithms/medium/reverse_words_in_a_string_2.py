from typing import List

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_elements(i, j):
            left, right = i, j
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        # 1) Handle corner case first
        if ' ' not in s:
            print(s)
            return
        N = len(s)
        # 2) Reverse individual words
        left, right = 0, 0
        while right < N:
            if s[right] == ' ':
                reverse_elements(left, right - 1)
                left = right + 1
            right += 1
        reverse_elements(left, right - 1)
        # 3) Finally, reverse the entire string
        reverse_elements(0, N - 1)
        print(s)

# Main section
for s in [
            ['t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'],
            ['a'],
            ['h','e','l','l','o',' ','w','o','r','l','d'],
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.reverseWords(s)
    print(f'r = {r}')
    print('============================')






