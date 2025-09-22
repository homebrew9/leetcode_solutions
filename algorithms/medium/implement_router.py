from typing import List
from collections import deque, defaultdict
from sortedcontainers import SortedList

class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.seen = set()
        self.dq = deque()
        self.hsh = defaultdict(SortedList)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        tpl = (source, destination, timestamp)
        if tpl in self.seen:
            return False
        if len(self.dq) == self.memory_limit:
            earliest_tuple = self.dq.popleft()
            self.seen.remove(earliest_tuple)
            (s, d, t) = earliest_tuple
            self.hsh[d].pop(0)
        self.dq.append(tpl)
        self.seen.add(tpl)
        sl = self.hsh[destination]
        sl.add(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.dq) == 0:
            return []
        tpl = self.dq.popleft()
        self.seen.remove(tpl)
        _, d, t = tpl
        self.hsh[d].pop(0)
        return list(tpl)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        sl = self.hsh[destination]
        #return len(list(sl.irange(startTime, endTime)))  # This is SLOWER than sl.bisect_* and throws TLE
        return sl.bisect_right(endTime) - sl.bisect_left(startTime)

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)

# Main section
#  ['Router','addPacket','addPacket','addPacket','addPacket','addPacket','forwardPacket','addPacket','getCount']
#  [[3],[1,4,90],[2,5,90],[1,4,90],[3,5,95],[4,5,105],[],[5,2,110],[5,100,110]]
#  ['Router','addPacket','forwardPacket','forwardPacket']
#  [[2],[7,4,90],[],[]]


