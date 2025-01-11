from typing import List, Optional

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec1 has points A and B at bottom-left and top-right locations
        ax, ay = rec1[0], rec1[1]
        bx, by = rec1[2], rec1[3]

        # rec2 has points C and D at bottom-left and top-right locations
        cx, cy = rec2[0], rec2[1]
        dx, dy = rec2[2], rec2[3]

        # rec2 is ABOVE rec1 or
        # rec2 is BELOW rec1 or
        # rec2 is TO THE LEFT OF rec1 or
        # rec2 is TO THE RIGHT OF rec1
        if cy >= by or dy <= ay or dx <= ax or cx >= bx:
            return False
        else:
            return True

# Main section
for rec1, rec2 in [
                     ([0,0,2,2], [1,1,3,3]),
                     ([0,0,1,1], [1,0,2,1]),
                     ([0,0,1,1], [2,2,3,3]),
                     ([0,0,1,1], [0,0,1,1]),
                     ([7,8,13,15], [10,8,12,20]),
                  ]:
    print(f'rec1 = {rec1} ; rec2 = {rec2}')
    sol = Solution()
    r = sol.isRectangleOverlap(rec1, rec2)
    print(f'r = {r}')
    print('==========================')

