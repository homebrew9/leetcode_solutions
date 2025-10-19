from heapq import heappush, heappop
from typing import List

class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        # Problem uses 1-indexed description, but coins is 0-indexed in code
        # So index 0 = position 1, index n-1 = position n
        if coins[0] == -1 or coins[-1] == -1:
            return []
        
        # Min-heap: (total_cost, path_as_tuple, current_index)
        heap = [(coins[0], (0,), 0)]  # start at index 0 (position 1)
        # Optional: track best cost to prune
        min_cost = [float('inf')] * n
        min_cost[0] = coins[0]
        
        while heap:
            cost, path_tuple, i = heappop(heap)
            
            # If we reached the last index, return 1-indexed path
            if i == n - 1:
                return [x + 1 for x in path_tuple]  # convert to 1-indexed
            
            # Prune if we've seen a better cost (or same cost with better lex path)
            # Note: heap ensures first time we pop n-1 is optimal
            if cost > min_cost[i]:
                continue
            
            # Explore next jumps
            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[j] == -1:
                    continue
                new_cost = cost + coins[j]
                new_path = path_tuple + (j,)
                
                # Only push if it's better cost, or same cost (heap handles lex via tuple)
                if new_cost < min_cost[j]:
                    min_cost[j] = new_cost
                    heappush(heap, (new_cost, new_path, j)) # type: ignore
                elif new_cost == min_cost[j]:
                    # Heap will naturally prefer lexicographically smaller tuple
                    heappush(heap, (new_cost, new_path, j)) # type: ignore
        
        return []

# Main section
for coins, maxJump in [
                         ([1,2,4,-1,2], 2),
                         ([1,2,4,-1,2], 1),
                      ]:
    print(f'coins, maxJump = {coins}, {maxJump}')
    sol = Solution()
    r = sol.cheapestJump(coins, maxJump)
    print(f'r = {r}')
    print('=====================')
























