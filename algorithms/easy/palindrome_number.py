class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr = list()
        while x > 0:
            q, r = divmod(x, 10)
            arr.append(r)
            x = q
        return arr == arr[::-1]

# Main section
for x in [
            121,
            -121,
            10,
            0,
         ]:
    print(f'x = {x}')
    sol = Solution()
    r = sol.isPalindrome(x)
    print(f'r = {r}')
    print('=====================')











