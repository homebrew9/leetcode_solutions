from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0
        
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0
            
            # Find all the balloons having the same color as the 
            # balloon indexed at i, record the total removal time 
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            
            # Once we reach the end of the current group, add the cost of 
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j
        
        return total_time

# Main section
for colors, neededTime in [
                             ('abaac', [1,2,3,4,5]),
                             ('abc', [1,2,3]),
                             ('aabaa', [1,2,3,4,1]),
                          ]:
    print(f'colors, neededTime = {colors}, {neededTime}')
    sol = Solution()
    r = sol.minCost(colors, neededTime)
    print(f'r = {r}')
    print('=====================')













