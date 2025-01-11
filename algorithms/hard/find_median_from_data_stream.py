from sortedcontainers import SortedList

class MedianFinder:
    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        mid = len(self.arr)//2
        if len(self.arr) % 2 == 1:
            return self.arr[mid]
        else:
            avg = (self.arr[mid-1] + self.arr[mid])/2
            return avg

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
r = mf.findMedian()
print(f'r = {r}')
mf.addNum(3)
r = mf.findMedian()
print(f'r = {r}')

