from typing import List
import collections

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        can_open = [status[i] == 1 for i in range(n)]
        has_box, used = [False] * n, [False] * n

        q = collections.deque()
        ans = 0
        for box in initialBoxes:
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                used[box] = True
                ans += candies[box]

        while len(q) > 0:
            big_box = q.popleft()
            for key in keys[big_box]:
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans += candies[key]
            for box in containedBoxes[big_box]:
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]

        return ans

# Main section
for status, candies, keys, containedBoxes, initialBoxes in [
         ([1,0,1,0], [7,5,4,100], [[],[],[1],[]], [[1,2],[3],[],[]], [0]),
         ([1,0,0,0,0,0], [1,1,1,1,1,1], [[1,2,3,4,5],[],[],[],[],[]], [[1,2,3,4,5],[],[],[],[],[]], [0]),
    ]:
    print(f'status = {status}')
    print(f'candies = {candies}')
    print(f'keys = {keys}')
    print(f'containedBoxes = {containedBoxes}')
    print(f'initialBoxes = {initialBoxes}')
    sol = Solution()
    r = sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(f'r = {r}')
    print('=======================')










