class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search
        low = 1
        high = int(num/2)
        while low < high:
            mid = int((low + high)/2)
            if mid*mid == num:
                return True
            if mid*mid < num:
                low = mid + 1
            elif mid*mid > num:
                high = mid - 1
        return low*low == num

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
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
           ]:
    print(f'num = {num}')
    r = sol.isPerfectSquare(num)
    print(f'r = {r}')
    print('======================')



