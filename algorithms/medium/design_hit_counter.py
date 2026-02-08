import bisect

class HitCounter:
    def __init__(self):
        self.arr = list()

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        val = timestamp - 300 + 1
        idx = bisect.bisect_left(self.arr, val)
        return len(self.arr) - idx

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# Main section
#  ['HitCounter','hit','hit','hit','getHits','hit','getHits','getHits']
#  [[],[1],[2],[3],[4],[300],[300],[301]]






