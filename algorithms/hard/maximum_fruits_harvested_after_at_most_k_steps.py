from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] <= startPos:
                return startPos - fruits[left][0]
            elif fruits[left][0] >= startPos:
                return fruits[right][0] - startPos
            else:
                return (
                    min(
                        abs(startPos - fruits[right][0]),
                        abs(startPos - fruits[left][0]),
                    )
                    + fruits[right][0]
                    - fruits[left][0]
                )

        # each time fix the right boundary of the window
        while right < n:
            sum += fruits[right][1]
            # move left boundary
            while left <= right and step(left, right) > k:
                sum -= fruits[left][1]
                left += 1

            ans = max(ans, sum)
            right += 1

        return ans

# Main section
for fruits, startPos, k in [
                              ([[2,8],[6,3],[8,6]], 5, 4),
                              ([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4),
                              ([[0,3],[6,4],[8,5]], 3, 2),
                           ]:
    print(f'fruits, startPos, k = {fruits}, {startPos}, {k}')
    sol = Solution()
    r = sol.maxTotalFruits(fruits, startPos, k)
    print(f'r = {r}')
    print('================')






