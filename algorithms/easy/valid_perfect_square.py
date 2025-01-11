class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Brute force method
        for i in range(num+1):
            if i*i == num:
                return True
            elif i*i > num:
                return False

# Main section
sol = Solution()
for num in [
              16,
              2147395600,
              1,
              1867104100,
              145,
              362,
              1295064168,
              680635927,
           ]:
    print(f'num = {num}')
    r = sol.isPerfectSquare(num)
    print(f'r = {r}')
    print('======================')

