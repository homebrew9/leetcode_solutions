#
# Doesn't work for the last test case.
# It's easier to determine the condition for non-overlap!
#
from typing import List, Optional

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1 == rec2:
            return True

        # rec1 has points A and B at bottom-left and top-right locations
        ax, ay = rec1[0], rec1[1]
        bx, by = rec1[2], rec1[3]

        # rec2 has points C and D at bottom-left and top-right locations
        cx, cy = rec2[0], rec2[1]
        dx, dy = rec2[2], rec2[3]

        # A inside C and D or
        # B inside C and D or
        # C inside A and B or
        # D inside A and B   ==> triangles overlap
        if (cx < ax < dx and cy < ay < dy) or (cx < bx < dx and cy < by < dy) or (ax < cx < bx and ay < cy < by) or (ax < dx < bx and ay < dy < by):
        #if (cx <= ax <= dx and cy <= ay <= dy) or (cx <= bx <= dx and cy <= by <= dy) or (ax <= cx <= bx and ay <= cy <= by) or (ax <= dx <= bx and ay <= dy <= by):
            return True
        else:
            return False

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

