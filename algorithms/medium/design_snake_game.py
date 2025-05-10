from typing import List
from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.dq = deque()
        self.dq.append((0, 0))
        self.score = 0
        self.width = width
        self.height = height
        self.food = food
        self.pos = 0
        self.hsh = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}
    def move(self, direction: str) -> int:
        r, c = self.dq[0]
        rnew, cnew = r + self.hsh[direction][0], c + self.hsh[direction][1]
        if not (0 <= rnew < self.height and 0 <= cnew < self.width):
            return -1
        if self.pos is not None and [rnew, cnew] == self.food[self.pos]:
            self.dq.appendleft((rnew, cnew))
            self.score += 1
            self.pos += 1
            if self.pos >= len(self.food):
                self.pos = None
            return self.score
        self.dq.pop()
        if (rnew, cnew) in self.dq:
            return -1
        self.dq.appendleft((rnew, cnew))
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

#["SnakeGame","move","move","move","move","move","move"]
#[[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]




