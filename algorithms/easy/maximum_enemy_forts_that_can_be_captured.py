from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_count = 0
        in_move = False
        for num in forts:
            if in_move:
                if num == 0:
                    curr += 1
                elif from_val == 1 and num == 1:
                    curr = 0
                    from_val = num
                elif from_val == 1 and num == -1:
                    max_count = max(max_count, curr)
                    curr = 0
                    from_val = num
                elif from_val == -1 and num == 1:
                    max_count = max(max_count, curr)
                    curr = 0
                    from_val = num
                elif from_val == -1 and num == -1:
                    curr = 0
                    from_val = num
            elif num in (1, -1):
                in_move = True
                curr = 0
                from_val = num
        return max_count

# Main section
for forts in [
                [1,0,0,-1,0,0,0,0,1],
                [0,0,1,-1],
                [0,0,0,0],
                [0,0,0,1],
                [1,0,0,1],
                [-1,0,0,1],
                [-1,0,-1,1],
                [1,0,0,-1,0,0,-1,0,0,1],
             ]:
    print(f'forts = {forts}')
    sol = Solution()
    r = sol.captureForts(forts)
    print(f'r = {r}')
    print('================')

