from sortedcontainers import SortedList
from collections import defaultdict

class Leaderboard:
    def __init__(self):
        self.sl = SortedList()
        self.hsh = defaultdict(list)

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hsh:
            self.sl.add((score, playerId))
        else:
            curr, idx = self.hsh[playerId]
            self.sl.pop(idx)
            self.sl.add((curr + score, playerId))
        self.hsh = {id: [score, i] for i, (score, id) in enumerate(self.sl)}
        
    def top(self, K: int) -> int:
        return sum([s for s, _ in self.sl[-K:]])

    def reset(self, playerId: int) -> None:
        _, idx = self.hsh[playerId]
        self.sl.pop(idx)
        self.hsh = {id: [score, i] for i, (score, id) in enumerate(self.sl)}

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)


# Main section
#  # Testcase 1
#  ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
#  [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
#  # Output 1
#  [null,null,null,null,null,null,73,null,null,null,141]
#  
#  # Testcase 2
#  ["Leaderboard","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","addScore","top","reset","reset","addScore","reset"]
#  [[],[1,13],[2,93],[3,84],[4,6],[5,89],[6,31],[7,7],[8,1],[9,98],[10,42],[5],[1],[2],[3,76],[4,68],[1],[3],[4],[2,70],[2]]
#  # Output 2
#  [null,null,null,null,null,null,null,null,null,null,null,406,null,null,null,null,160,null,null,null,null]
#  




