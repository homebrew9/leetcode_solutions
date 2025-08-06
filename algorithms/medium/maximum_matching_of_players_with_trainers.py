from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count

# Main section
for players, trainers in [
                            ([4,7,9], [8,2,5,8]),
                            ([1,1,1], [10]),
                         ]:
    print(f'players  = {players}')
    print(f'trainers = {trainers}')
    sol = Solution()
    r = sol.matchPlayersAndTrainers(players, trainers)
    print(f'r = {r}')
    print('================')








