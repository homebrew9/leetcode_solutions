from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # For each character we iterate through, we find out the
        # distance between its current and next occurrence, and
        # compare that value with distance array.
        for i, ch in enumerate(s):
            next_occurrence = s.find(ch, i+1)
            if next_occurrence >= 0:
                if distance[ord(ch)-97] != next_occurrence - i - 1:
                    return False
        return True

# Main section
for s, distance in [
                      ('abaccb', [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
                      ('aa', [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
                   ]:
    print(f's, distance = {s}, {distance}')
    sol = Solution()
    r = sol.checkDistances(s, distance)
    print(f'r = {r}')
    print('=====================')

