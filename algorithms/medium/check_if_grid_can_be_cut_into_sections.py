from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        '''
            [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
            sorted(rectangles)
            [[0, 2, 2, 4], [0, 4, 4, 5], [1, 0, 5, 2], [3, 2, 5, 3]]
            sorted(rectangles, key=lambda x: (x[1], x[3]))
            [[1, 0, 5, 2], [3, 2, 5, 3], [0, 2, 2, 4], [0, 4, 4, 5]]
        '''
        N = len(rectangles)
        # Can we can make two vertical cuts?
        rectangles.sort()
        res = 0
        for i in range(N):
            startx, starty, endx, endy = rectangles[i]
            if i == 0:
                start = startx
                end = endx
            else:
                if startx < end:
                    end = max(end, endx)
                else:
                    res += 1
                    if res >= 2:
                        return True
                    start, end = startx, endx
        # Can we can make two horizontal cuts?
        rectangles.sort(key=lambda x: (x[1], x[3]))
        res = 0
        for i in range(N):
            startx, starty, endx, endy = rectangles[i]
            if i == 0:
                start = starty
                end = endy
            else:
                if starty < end:
                    end = max(end, endy)
                else:
                    res += 1
                    if res >= 2:
                        return True
                    start, end = starty, endy
        # If we are here, neither vertical nor horizontal cut is possible.
        return False

# Main section
for n, rectangles in [
                        (5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]),
                        (4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]),
                        (4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]),
                     ]:
    print(f'n, rectangles = {n}, {rectangles}')
    sol = Solution()
    r = sol.checkValidCuts(n, rectangles)
    print(f'r = {r}')
    print('========================')

