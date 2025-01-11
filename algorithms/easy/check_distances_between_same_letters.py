from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hsh = dict()
        for i, ch in enumerate(s):
            if not ch in hsh:
                hsh[ch] = i
            else:
                dist = i - hsh[ch] - 1
                if distance[ord(ch)-97] != dist:
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

