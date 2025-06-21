class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_dist = 0
        countN, countS, countE, countW = 0, 0, 0, 0
        for i, move in enumerate(s):
            if move == 'N':
                countN += 1
            elif move == 'S':
                countS += 1
            elif move == 'E':
                countE += 1
            else: # move == 'W'
                countW += 1
            
            # Number of steps taken so far
            L = i + 1

            # Calculate total conflicting pairs
            min_pairs = min(countN, countS) + min(countE, countW)

            current_dist = 0
            if k >= min_pairs:
                # We can fix all conflicts
                current_dist = L
            else:
                # We can only fix k pairs
                # Start with distance from non-conflicting moves, add 2 for each fix
                base_dist_from_non_conflicting = L - 2 * min_pairs
                current_dist = base_dist_from_non_conflicting + 2 * k
            
            max_dist = max(max_dist, current_dist)
        
        return max_dist

# Main section
for s, k in [
               ('NWSE', 1),
               ('NSWWEW', 3),
               ('NSES', 1),
               ('EWWE', 1),
               ('WEEW', 3),
               ('WEWE', 1),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.maxDistance(s, k)
    print(f'r = {r}')
    print('=======================')










