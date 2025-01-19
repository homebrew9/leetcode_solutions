from sortedcontainers import SortedList
from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hsh = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hsh[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hsh[key]
        N = len(arr)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return '' if right < 0 else self.hsh[key][right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


